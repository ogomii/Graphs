from email.generator import Generator
import tkinter as tk
from tkinter import INSERT, filedialog as fd
import pathlib

from Graph import Graph, GraphTypes
from Converter import Converter
from Generator import Generator

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.graph = Graph

        self.title('Graphs - Project 1')
        self.geometry('1360x720')

        self.create_widgets()

    def load_from_file(self) -> None:
        # Allowed file types
        file_types = (
            ("Adjacency List", "*.adjl"),
            ("Adjacency Matrix", "*.adjm"),
            ("Incidence Matrix", "*.incm")
        )

        file = fd.askopenfile(
            title="Open a file",
            initialdir=".",
            filetypes=file_types
        )

        # File opened 
        if file:
            self.reset_buttons()

            # File extension without dot character
            extension = pathlib.Path(file.name).suffix[1:]

            # Loading file to corresponding structure
            if extension == 'adjl':
                self.to_adjacency_list_button.config(state=tk.DISABLED)
                self.graph.content = Graph.load_adjacency_list(file.name)
                self.graph.type = GraphTypes.AdjacencyList
                self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content))
            elif extension == 'adjm':
                self.to_adjacency_matrix_button.config(state=tk.DISABLED)
                self.graph.content = Graph.load_adjacency_matrix(file.name)
                self.graph.type = GraphTypes.AdjacencyMatrix
                self.graph_text_output.insert(INSERT, Graph.adjacency_matrix_to_str(self.graph.content))
            elif extension == 'incm':
                self.to_incidence_matrix_button.config(state=tk.DISABLED)
                self.graph.content = Graph.load_incidence_matrix(file.name)
                self.graph.type = GraphTypes.IncidenceMatrix
                self.graph_text_output.insert(INSERT, Graph.incidence_matrix_to_str(self.graph.content))
            else:
                print("Unknown Error")
                exit(-1)

    def to_adj_matrix(self) -> None:
        if self.graph.type == GraphTypes.AdjacencyList:
            self.graph.content = Converter.adj_list_to_adj_matrix(self.graph.content)     
        elif self.graph.type == GraphTypes.IncidenceMatrix:
            self.graph.content = Converter.inc_matrix_to_adj_matrix(self.graph.content)

        self.reset_buttons()
        self.graph.type = GraphTypes.AdjacencyMatrix
        self.to_adjacency_matrix_button.config(state=tk.DISABLED)
        self.graph_text_output.insert(INSERT, Graph.adjacency_matrix_to_str(self.graph.content))    

    def to_adj_list(self) -> None:
        if self.graph.type == GraphTypes.AdjacencyMatrix:
            self.graph.content = Converter.adj_matrix_to_adj_list(self.graph.content)     
        elif self.graph.type == GraphTypes.IncidenceMatrix:
            self.graph.content = Converter.inc_matrix_to_adj_list(self.graph.content)

        self.reset_buttons()
        self.graph.type = GraphTypes.AdjacencyList
        self.to_adjacency_list_button.config(state=tk.DISABLED)
        self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content)) 

    def to_inc_matrix(self) -> None:
        if self.graph.type == GraphTypes.AdjacencyList:
            self.graph.content = Converter.adj_list_to_inc_matrix(self.graph.content)     
        elif self.graph.type == GraphTypes.AdjacencyMatrix:
            self.graph.content = Converter.adj_matrix_to_inc_matrix(self.graph.content)

        self.reset_buttons()
        self.graph.type = GraphTypes.IncidenceMatrix
        self.to_incidence_matrix_button.config(state=tk.DISABLED)
        self.graph_text_output.insert(INSERT, Graph.incidence_matrix_to_str(self.graph.content))

    def generate_graph_np(self):
        self.graph.type = GraphTypes.IncidenceMatrix
        self.graph.content = Generator.generate_np(int(self.n_input.get()), float(self.lp_input.get()))

        self.reset_buttons()
        self.to_incidence_matrix_button.config(state=tk.DISABLED)
        self.graph_text_output.insert(INSERT, Graph.incidence_matrix_to_str(self.graph.content))

    def generate_graph_nl(self): 
        self.graph.type = GraphTypes.IncidenceMatrix
        self.graph.content = Generator.generate_nl(int(self.n_input.get()), int(self.lp_input.get()))

        self.reset_buttons()
        self.to_incidence_matrix_button.config(state=tk.DISABLED)
        self.graph_text_output.insert(INSERT, Graph.incidence_matrix_to_str(self.graph.content))

    def reset_buttons(self) -> None:
        self.graph_text_output.delete('1.0', 'end')
        self.to_adjacency_list_button.config(state=tk.ACTIVE)
        self.to_adjacency_matrix_button.config(state=tk.ACTIVE)
        self.to_incidence_matrix_button.config(state=tk.ACTIVE)

    def create_widgets(self) -> None:
        self.load_button = tk.Button(self, text='Load from file', command=self.load_from_file)
        self.load_button.grid(column=0, row=0, padx=10, pady=10)

        self.n_label = tk.Label(self, text='N: ')
        self.n_label.grid(column=0, row=1)

        self.n_input = tk.Entry(self)
        self.n_input.grid(column=1, row=1)

        self.lp_label = tk.Label(self, text='L/P: ')
        self.lp_label.grid(column=0, row=2)

        self.lp_input = tk.Entry(self)
        self.lp_input.grid(column=1, row=2)

        self.generate_gnl_button = tk.Button(self, text='Generate G(n, l)', command=self.generate_graph_nl)
        self.generate_gnl_button.grid(column=0, row=3, padx=10, pady=10)

        self.generate_gnp_button = tk.Button(self, text='Generate G(n, p)', command=self.generate_graph_np)
        self.generate_gnp_button.grid(column=1, row=3, padx=10, pady=10)

        self.to_adjacency_list_button = tk.Button(self, text='To adjacency list', command=self.to_adj_list)
        self.to_adjacency_list_button.grid(column=0, row=4, padx=10, pady=10)

        self.to_adjacency_matrix_button = tk.Button(self, text='To adjacency matrix', command=self.to_adj_matrix)
        self.to_adjacency_matrix_button.grid(column=0, row=5, padx=10, pady=10)

        self.to_incidence_matrix_button = tk.Button(self, text='To incidence matrix', command=self.to_inc_matrix)
        self.to_incidence_matrix_button.grid(column=0, row=6, padx=10, pady=10)

        self.visualize_button = tk.Button(self, text='Visualize Graph')
        self.visualize_button.grid(column=0, row=7, padx=10, pady=10)

        self.graph_text_output = tk.Text(self, width=40, height=20)
        self.graph_text_output.grid(column=2, row=0, rowspan=14, padx=10, pady=10)

        self.graph_image_output = tk.Canvas(self, bg='white', width=600, height=600)
        self.graph_image_output.grid(column=3, row=0, rowspan=14, padx=10, pady=10)
