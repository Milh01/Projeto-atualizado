import os
from biblioteca.grafo import Grafo

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def executar_dijkstra():
    clear()
    g = Grafo("entrada/grafo.json")

    print("Nós disponíveis:", ", ".join(g.graph.keys()))
    start = input("Digite o nó inicial: ")
    goal = input("Digite o nó final: ")

    try:
        result = g.dijkstra(start, goal)
        print("\n=== RESULTADO DIJKSTRA ===")
        print("Caminho encontrado:", " -> ".join(result["caminho"]))
        print("Custo total:", result["custo"])
        print("Tempo de execução: %.6f segundos" % result["tempo"])
    except ValueError as e:
        print("\nErro:", e)

def executar_busca_informada():
    clear()
    g = Grafo("entrada/grafo.json")

    print("Nós disponíveis:", ", ".join(g.graph.keys()))
    start = input("Digite o nó inicial: ")
    goal = input("Digite o nó final: ")

    try:
        result = g.busca_informada(start, goal)
        print("\n=== RESULTADO BUSCA INFORMADA (A*) ===")
        print("Caminho encontrado:", " -> ".join(result["caminho"]))
        print("Custo total:", result["custo"])
        print("Tempo de execução: %.6f segundos" % result["tempo"])
    except ValueError as e:
        print("\nErro:", e)

def main():
    r = "s"
    while r == "s":
        clear()
        print("\nDigite qual algoritmo deseja utilizar:")
        print("[1] Dijkstra")
        print("[2] Busca Informada")

        try:
            a = int(input("Escolha: "))
        except ValueError:
            print("\nInsira um número válido!!!")
            a = 0

        if a == 1:
            executar_dijkstra()
        elif a == 2:
            executar_busca_informada()
        else:
            print("\nInsira um número válido!!!")

        input("\nPressione ENTER para continuar...")
        clear()
        r = input("\nDeseja buscar novamente? (s/n): ").lower()

if __name__ == "__main__":
    main()
