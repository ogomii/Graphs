from Converter import Converter
from Graph import Graph, GraphTypes

def generate_regular_graph(vertices_amount: int, vertices_degree: int):
    graph = Graph()
    
    sequence = [vertices_degree] * vertices_amount
    graph.content = Converter.sequence_to_adj_list(sequence)
    graph.type = GraphTypes.AdjacencyList
    graph.randomize(100)

    return graph