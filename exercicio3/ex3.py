print('-=-=-= Exercício 3 -=-=-=')
import sys

def calcular_dijkstra(grafo, origem):
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    visitados = set()

    while visitados != set(distancias):
        vertice_atual = None
        menor_distancia = sys.maxsize
        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]
                
        visitados.add(vertice_atual)

        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso
    return distancias


grafo = {
  'A': {'B': 5, 'C': 3, 'D': 2},
  'B': {'A': 5, 'C': 2, 'E': 4},
  'C': {'A': 3, 'B': 2, 'D': 1},
  'D': {'A': 2, 'C': 1, 'E': 7},
  'E': {'B': 4, 'D': 7}
}

origem = 'A'

caminhos_mais_curto = calcular_dijkstra(grafo, origem)

for destino, distancia in caminhos_mais_curto.items():
  print(f"Caminho mais curto de {origem} para {destino}: {distancia}")

import sys
print(sys.argv[0])
print('Number of arguments present =', len(sys.argv))
print('Total argument list:', str(sys.argv))