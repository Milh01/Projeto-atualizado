import json
import time
import heapq
from typing import Dict, List, Tuple

class Grafo:
    def __init__(self, file_path: str):
        with open(file_path, "r") as f:
            self.data = json.load(f)

        self.graph: Dict[str, List[Tuple[str, float]]] = {}
        self.heuristica: Dict[str, float] = self.data.get("heuristica", {})

        # Inicializa os nós
        for node in self.data.keys():
            if node != "heuristica":
                self.graph[node] = []

        # Adiciona as arestas
        for node, info in self.data.items():
            if node == "heuristica":
                continue
            for neighbor, weight in info["arestas"].items():
                self.graph[node].append((neighbor, weight))
                if neighbor not in self.graph:
                    self.graph[neighbor] = []

    def dijkstra(self, start: str, goal: str) -> dict:
        start_time = time.time()

        if start not in self.graph or goal not in self.graph:
            raise ValueError("Nó inicial ou final não existe no grafo.")

        dist = {node: float("inf") for node in self.graph}
        dist[start] = 0
        parent = {node: None for node in self.graph}

        pq = [(0, start)]

        while pq:
            d, u = heapq.heappop(pq)
            if u == goal:
                break
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))

        # Reconstruir caminho
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

        exec_time = time.time() - start_time

        return {
            "custo": dist[goal],
            "caminho": path,
            "tempo": exec_time
        }

    def busca_informada(self, start: str, goal: str) -> dict:
        """Implementa A* (Busca Informada com heurística)"""
        start_time = time.time()

        if start not in self.graph or goal not in self.graph:
            raise ValueError("Nó inicial ou final não existe no grafo.")

        g_score = {node: float("inf") for node in self.graph}
        g_score[start] = 0
        parent = {node: None for node in self.graph}

        # F(n) = G(n) + H(n)
        f_score = {node: float("inf") for node in self.graph}
        f_score[start] = self.heuristica.get(start, 0)

        pq = [(f_score[start], start)]

        while pq:
            _, u = heapq.heappop(pq)
            if u == goal:
                break
            for v, w in self.graph[u]:
                tent_g = g_score[u] + w
                if tent_g < g_score[v]:
                    parent[v] = u
                    g_score[v] = tent_g
                    f_score[v] = g_score[v] + self.heuristica.get(v, 0)
                    heapq.heappush(pq, (f_score[v], v))

        # Reconstruir caminho
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

        exec_time = time.time() - start_time

        return {
            "custo": g_score[goal],
            "caminho": path,
            "tempo": exec_time
        }
