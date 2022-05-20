import tkinter as tk
from Graph import Graph

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.graph = Graph()
        self.title('Graphs - Project 1')

        self.create_widgets()
        self.generate_random_connected_graph()

    def generate_random_connected_graph(self) -> None:
        """Generates randomized connected graph with random weights ranging from 1 to 10"""
        self.graph.create_random_graph()
        self.graph.visualize()
        return
    
    def  get_dijkstra_path(self) -> None:
        """calculates shortest paths from given vertex to all vertices"""
        selectedVertex = int(self.vertex_entry.get())
        bestPaths = self.graph.getPathsFrom(selectedVertex)
        self.graph_text_output.delete('1.0', 'end')
        self.graph_text_output.insert(tk.INSERT, bestPaths)
        return
    
    def get_distance_matrix(self) -> None:
        matrix = self.graph.getDistMatrix()
        self.graph_text_output.delete('1.0', 'end')
        self.graph_text_output.insert(tk.INSERT, matrix)
        return

    def get_grap_center(self) -> None:
        center = self.graph.getCenter()
        self.graph_text_output.delete('1.0', 'end')
        self.graph_text_output.insert(tk.INSERT, center)
    
    def get_minimax(self) -> None:
        minimax = self.graph.getMinimax()
        self.graph_text_output.delete('1.0', 'end')
        self.graph_text_output.insert(tk.INSERT, minimax)

    def get_min_span_tree(self) -> None:
        self.graph.drawMinSpanTree()

    def create_widgets(self) -> None:

        self.graph_text_output = tk.Text(self, width=100, height=50)
        self.graph_text_output.grid(column=2, row=0, rowspan=14, padx=10, pady=10)

        self.generate_random_connected_graph_button = tk.Button(self, text='Random connected graph', command=self.generate_random_connected_graph)
        self.generate_random_connected_graph_button.grid(column=1, row=1, padx=10, pady=10)

        self.vertex_label = tk.Label(self, text='vertex entry: ')
        self.vertex_label.grid(column=0, row=3, padx=10, pady=10)
        self.vertex_entry = tk.Entry(self)
        self.vertex_entry.grid(column=1, row=3, padx=10, pady=10)

        self.dijsktra_path_button = tk.Button(self, text='Dijkstra path', command=self.get_dijkstra_path)
        self.dijsktra_path_button.grid(column=1, row=4, padx=10, pady=10)
        
        self.distance_matrix_button = tk.Button(self, text='Distance matrix', command=self.get_distance_matrix)
        self.distance_matrix_button.grid(column=1, row=5, padx=10, pady=10)

        self.graph_center_button = tk.Button(self, text='Graph center', command=self.get_grap_center)
        self.graph_center_button.grid(column=1, row=6, padx=10, pady=10)

        self.graph_minimax_button = tk.Button(self, text='Minimax', command=self.get_minimax)
        self.graph_minimax_button.grid(column=1, row=7, padx=10, pady=10)

        self.graph_min_span_tree_button = tk.Button(self, text='Min span tree', command=self.get_min_span_tree)
        self.graph_min_span_tree_button.grid(column=1, row=8, padx=10, pady=10)