import networkx as nx
from matplotlib import pylab
import pylab as plt
import numpy as np


def calculateVertexesCoordinates(graph, radius):
    """
    Zwraca wspolrzedne wierzcholkow dla danego grafu oraz promienia
    """
    numberOfVertexes = graph.getNumberOfVertexes()
    coordinates = [
        (np.sin(np.pi * 2 * i / numberOfVertexes) * radius, np.cos(np.pi * 2 * i / numberOfVertexes) * radius) for i in
        range(numberOfVertexes)]
    return coordinates


def drawVertexes(graph, radius, filename):
    """
    Dokonuje konwersji z typu Graph na networkx.Graph().
    Zapisuje wizualizacje grafu do pliku o podanej nazwie
    """
    g = nx.Graph()
    vertexValue = 1
    coordinates = calculateVertexesCoordinates(graph, radius)
    for Vertex in graph.vertexIndex:
        g.add_node(Vertex, pos=coordinates[vertexValue - 1])
        vertexValue = - 1
    for i in range(len(graph.vertexIndex)):
        i += 1
        for j in range(len(graph.vertexIndex)):
            j += 1
            if i != j:
                if graph.findEdges('v' + str(i), 'v' + str(j)) is not None:
                    startVertex = 'v' + str(i)
                    endVertex = 'v' + str(j)
                    print(graph.findEdges('v' + str(i), 'v' + str(j)))
                    g.add_edge(startVertex, endVertex)

    pos = nx.circular_layout(g)
    nx.draw(g, with_labels=True, pos=pos)
    plt.savefig(filename)
    plt.clf()
