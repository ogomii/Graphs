import math
import tkinter as tk
import numpy as np
from collections import defaultdict
from enum import Enum
from Converter import Converter

class GraphTypes(Enum):
    AdjacencyList = 1,
    AdjacencyMatrix = 2,
    IncidenceMatrix = 3

class Graph:
    def __init__(self):
        self.content = None
        self.type = None

    def visualize(self, canvas: tk.Canvas) -> None:
        canvas.delete('all')

        graph_copy = defaultdict(list)

        if self.type is GraphTypes.AdjacencyMatrix:
            graph_copy = Converter.adj_matrix_to_adj_list(self.content)
        if self.type is GraphTypes.IncidenceMatrix:
            graph_copy = Converter.inc_matrix_to_adj_list(self.content)
        else:
            graph_copy = self.content

        vertices_number = len(graph_copy)
        center_x = canvas.winfo_width() / 2
        center_y = canvas.winfo_height() / 2 
        radius = min(center_x, center_y) / 1.25
        angle = 2 * math.pi / vertices_number

        for i in range(1, vertices_number+1):
            current_angle = i * angle
            x = center_x + radius * math.sin(current_angle)
            y = center_y - radius * math.cos(current_angle)

            for connected_edge in graph_copy[i]:
                connected_edge_angle = angle * connected_edge
                connected_edge_x = center_x + radius * math.sin(connected_edge_angle)
                connected_edge_y = center_y - radius * math.cos(connected_edge_angle)

                canvas.create_line(x, y, connected_edge_x, connected_edge_y)

            canvas.create_oval(x-20, y-20, x+20, y+20, outline='black', fill='white', width=1)
            canvas.create_text(x, y, text=str(i))

    @staticmethod
    def load_adjacency_list(path:str) -> dict:
        adjacency_list = defaultdict(list)

        with open(path) as file:
            lines = file.readlines()
            counter = 1

            for line in lines:
                line = line.strip()
                line = line.split(' ')

                for element in line:
                    if not element.endswith('.'):
                        adjacency_list[counter].append(int(element))

                counter += 1

        return adjacency_list

    @staticmethod
    def adjacency_list_to_str(adj_list: dict) -> str:
        result: str = ''

        for key in adj_list:
            result += str(key) + '.'
            for element in adj_list[key]:
                result += ' ' + str(element)

            result += '\n'

        return result

    @staticmethod
    def load_adjacency_matrix(path:str) -> np.ndarray:
        adjacency_matrix:np.ndarray

        with open(path) as file:
            lines = file.readlines()
            size = len(lines)

            adjacency_matrix = np.zeros((size, size), int)

            for i in range(0, len(lines)):
                line = lines[i].strip()
                line = line.split(' ')

                for j in range(0, len(line)):
                    if int(line[j]) == 1:
                        adjacency_matrix[i][j] = 1

        return adjacency_matrix

    @staticmethod
    def adjacency_matrix_to_str(adj_matrix: np.ndarray) -> str:
        result: str = ''
        x, y = adj_matrix.shape
        
        for i in range(0, x):
            for j in range(0, y):
                result += str(adj_matrix[i][j]) + " "

            result += "\n"

        return result


    @staticmethod
    def load_incidence_matrix(path:str) -> np.ndarray:
        incidence_matrix:np.ndarray

        with open(path) as file:
            lines = file.readlines()
            size_x = len(lines)
            tmp = lines[0].strip()
            tmp = lines[0].split()
            size_y = len(tmp)

            incidence_matrix = np.zeros((size_x, size_y), int)

            for i in range(0, len(lines)):
                line = lines[i].strip()
                line = line.split(' ')

                for j in range(0, len(line)):
                    if int(line[j]) == 1:
                        incidence_matrix[i][j] = 1

        return incidence_matrix
    
    @staticmethod
    def incidence_matrix_to_str(inc_matrix: np.ndarray) -> str:
        result: str = ''
        x, y = inc_matrix.shape
        
        for i in range(0, x):
            for j in range(0, y):
                result += str(inc_matrix[i][j]) + " "

            result += "\n"

        return result
