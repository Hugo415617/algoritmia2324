import sys

from typing import TextIO

from algoritmia.datastructures.queues import Fifo

if sys.version_info.major != 3 or sys.version_info.minor < 10:
    raise RuntimeError("This program needs Python3, version 3.10 or higher")

from algoritmia.datastructures.graphs import UndirectedGraph

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def read_data(f: TextIO) -> tuple[UndirectedGraph[Vertex], int, int]:
    # TODO: IMPLEMENTAR

    # La Primera línea incluye filas y columnas.
    rows, cols = map(int, f.readline().strip().split())
    lineas = f.readlines()
    edges = [] #Creo el vector de aristas.
    vertices: list[Vertex] = [(row, col) for row in range(rows) for col in range(cols)]

    # A partir de aquí, cada línea es una fila del laberinto.
    for fila in range(rows):
        linea_vec = lineas[fila].strip()
        for columna in range(cols):
            celda = int(linea_vec[columna])

            # Diferencio según los casos descritos en el PDF de explicación.
            if celda == 1:
                if columna < cols:
                    edges.append(((fila, columna), (fila, columna+1)))

            elif celda == 2:
                if fila < rows:
                    edges.append(((fila, columna), (fila+1, columna)))

            elif celda == 3:
                if columna < cols:
                    edges.append(((fila, columna), (fila, columna + 1)))
                if fila < rows:
                    edges.append(((fila, columna), (fila + 1, columna)))

    return UndirectedGraph(V=vertices, E=edges), rows, cols #Devuelvo la tupla formada por el grafo no dirigido, el número de filas y el número de columnas.

def bf_search(ug: UndirectedGraph[Vertex], source: Vertex) -> tuple[dict[Vertex, Vertex], list[Edge]]:
    cola: Fifo[Edge] = Fifo()
    cola.push((source, source))

    vistos: set[Vertex] = set()
    vistos.add(source)

    camino: list[Edge] = list()
    bp: dict[Vertex, Vertex] = dict()

    while len(cola) > 0:
        u, v = cola.pop()
        camino.append((u, v))
        bp[v] = u

        succs = list(ug.succs(v))
        succs.sort() #Esto evita usar dirs???

        for succ in succs:
            if succ not in vistos:
                vistos.add(succ)
                cola.push((v, succ))
    return bp, camino

def calcula_pasos(bp: dict[Vertex, Vertex], distances: dict[(Vertex, Vertex), int], origen: Vertex, destino: Vertex) -> int:
    steps = 0
    if bp[destino] == origen:
        steps = 1
    elif bp[destino] == bp[origen]:
        steps = 2
    else:
        steps = distances[(bp[destino], origen)] + 1
    return steps

def process(ug: UndirectedGraph[Vertex], rows: int, cols: int) -> int:
    suma_steps = 0
    distances: dict[(Vertex, Vertex), int] = dict()
    bp, camino = bf_search(ug, (0, 0))

    ultimo_vertice = None

    for u, v in camino:
        if ultimo_vertice is not None:
            steps = calcula_pasos(bp, distances, ultimo_vertice, v)
            suma_steps += steps
            distances[(ultimo_vertice, v)] = steps
        ultimo_vertice = v

    return suma_steps

def show_results(steps: int):
    print(steps)


if __name__ == "__main__":
    ug0, rows0, cols0 = read_data(sys.stdin)
    steps0 = process(ug0, rows0, cols0)
    show_results(steps0)
