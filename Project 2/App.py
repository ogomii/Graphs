from email.generator import Generator
import tkinter as tk
from tkinter import INSERT, filedialog as fd

from sequnce import check_sequnce
from components import components, comp_to_string, find_biggest_comp
from Graph import Graph, GraphTypes
from Converter import Converter

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.graph = Graph()

        self.title('Graphs - Project 1')
        self.geometry('1360x720')

        self.create_widgets()

    def check_sequence_action(self) -> None:
        is_sequence = check_sequnce(self.sequence_entry.get())

        if is_sequence:
            self.sequence_check_answer['text'] = 'Sequnce'
            sequence = self.sequence_entry.get()
            sequence = sequence.strip()
            sequence = list(map(int, sequence.split(' ')))
            self.graph.content = Converter.sequence_to_adj_list(sequence)
            self.graph.type = GraphTypes.AdjacencyList

            self.graph_text_output.delete('1.0', 'end')
            self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content))
            self.graph.visualize(self.graph_image_output)

        elif not is_sequence:
            self.sequence_check_answer['text'] = 'Not sequnce'


    def randomize_graph(self) -> None:
        number = int(self.randomize_entry.get())
        self.graph.randomize(number)
        
        self.graph_text_output.delete('1.0', 'end')
        self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content))
        self.graph.visualize(self.graph_image_output)

    def get_components(self) -> None:
        if self.graph.type is GraphTypes.AdjacencyList:
            comp_list = components(self.graph.content)

            self.graph_text_output.delete('1.0', 'end')
            self.graph_text_output.insert(INSERT, comp_to_string(comp_list, self.graph.content))
            self.graph_text_output.insert(INSERT, 'Największa składowa ma numer: ' + str(find_biggest_comp(comp_list)))

    def create_widgets(self) -> None:
        self.sequnce_label = tk.Label(self, text='Sequence: ')
        self.sequnce_label.grid(column=0, row=0, padx=10, pady=10)

        self.sequence_entry = tk.Entry(self)
        self.sequence_entry.grid(column=1, row=0, padx=10, pady=10)
        self.sequence_entry.insert(INSERT, '4 2 2 3 2 1 4 2 2 2 2')

        self.sequence_check_button = tk.Button(self, text="Check sequence", command=self.check_sequence_action)
        self.sequence_check_button.grid(column=0, row=1, padx=10, pady=10)

        self.sequence_check_answer = tk.Label(self, text="")
        self.sequence_check_answer.grid(column=1, row=1, padx=10, pady=10)

        self.randomize_label = tk.Label(self, text='Randomize number: ')
        self.randomize_label.grid(column=0, row=2, padx=10, pady=10)

        self.randomize_entry = tk.Entry(self)
        self.randomize_entry.grid(column=1, row=2, padx=10, pady=10)

        self.randomize_button = tk.Button(self, text='Randomize graph', command=self.randomize_graph)
        self.randomize_button.grid(column=1, row=3, padx=10, pady=10)

        self.component_button = tk.Button(self, text='Get components', command=self.get_components)
        self.component_button.grid(column=0, row=4, padx=10, pady=10)

        self.graph_text_output = tk.Text(self, width=40, height=20)
        self.graph_text_output.grid(column=2, row=0, rowspan=14, padx=10, pady=10)

        self.graph_image_output = tk.Canvas(self, bg='white', width=600, height=600)
        self.graph_image_output.grid(column=3, row=0, rowspan=14, padx=10, pady=10)
