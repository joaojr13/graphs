import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from floyd_warshall import floyd_warshall

def main():

    inf = float("inf")

    grafo = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]
    ]

# Gerando a matriz de distâncias
    distancias = floyd_warshall(grafo, 4)

# Exibindo a matriz de distâncias resultante
    for linha in distancias:
        print(linha)

if __name__ == "__main__":
    main()