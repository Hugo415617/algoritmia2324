import sys

if sys.version_info.major != 3 or sys.version_info.minor < 10:
    raise RuntimeError("This program needs Python3, version 3.10 or higher")

from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def read_data(f: TextIO) -> tuple[UndirectedGraph[Vertex], int, int]:
    # TODO: IMPLEMENTAR

    print(f.readline())
    lineas = f.readlines()

    # La Primera línea incluye filas y columnas.
    rows, cols = map(int, lineas[0].strip().split())
    edges = [] #Creo el vector de aristas.

    # A partir de aquí, cada línea es una fila del laberinto.
    for fila in range(1, rows+1):
        linea_vec = lineas[fila].strip()
        for columna in range(cols):
            celda = int(linea_vec[columna])

            # Diferencio según los casos descritos en el PDF de explicación.
            if celda == 1:
                if columna < cols-1:
                    edges.append(((fila, columna), (fila, columna+1)))

            elif celda == 2:
                if fila < rows:
                    edges.append(((fila, columna), (fila+1, columna)))

            elif celda == 3:
                if columna < cols - 1:
                    edges.append(((fila, columna), (fila, columna + 1)))
                if fila < rows:
                    edges.append(((fila, columna), (fila + 1, columna)))

    return (UndirectedGraph(E=edges), rows, cols) #Devuelvo la tupla formada por el grafo no dirigido, el número de filas y el número de columnas.


def process(ug: UndirectedGraph[Vertex], rows: int, cols: int) -> int:
    # TODO: IMPLEMENTAR
    raise NotImplementedError


def show_results(steps: int):
    print(steps)


if __name__ == "__main__":
    ug0, rows0, cols0 = read_data(sys.stdin)
    steps0 = process(ug0, rows0, cols0)
    show_results(steps0)
