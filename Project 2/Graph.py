import math
from random import randint, random
from re import I
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

        if self.type is GraphTypes.AdjacencyList:
            graph_copy = self.content.copy()
        if self.type is GraphTypes.AdjacencyMatrix:
            graph_copy = Converter.adj_matrix_to_adj_list(self.content)
        if self.type is GraphTypes.IncidenceMatrix:
            graph_copy = Converter.inc_matrix_to_adj_list(self.content)


        vertices_number = len(graph_copy)
        center_x = canvas.winfo_width() / 2
        center_y = canvas.winfo_height() / 2 
        radius = min(center_x, center_y) / 1.25
        angle = 2 * math.pi / vertices_number

        positions: list = []

        canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='red', width=2, dash=(100, 50))

        for i in range(0, vertices_number):
            current_angle = i * angle
            x = center_x + radius * math.sin(current_angle)
            y = center_y - radius * math.cos(current_angle)
            
            for connected_edge in graph_copy[i + 1]:
                connected_edge = connected_edge - 1
                if(connected_edge > i):
                    conneted_angle = connected_edge * angle
                    connected_x = center_x + radius * math.sin(conneted_angle)
                    connected_y = center_y - radius * math.cos(conneted_angle)
                
                    canvas.create_line(x, y, connected_x, connected_y, width=3)
            
            positions.append((x, y))
            
        for i in range(0, vertices_number):
            x, y = positions[i]
            scale = 0.1
            pos = (x - radius * scale, y - radius * scale, x + radius * scale, y + radius * scale)
            canvas.create_oval(pos[0], pos[1], pos[2], pos[3], outline='#343aeb', fill='#6b7cc9', width=2.5)
            canvas.create_text(x, y, text=str(i + 1), font=('Arial',int(radius * scale/2),'bold'))

    def randomize(self, randomize_amount) -> None:
        for i in range(0, randomize_amount):
            edges = self.__get_random_edges()
            first_edge = edges[0]
            second_edge = edges[1]

            a = first_edge[0]
            b = first_edge[1]
            c = second_edge[0]
            d = second_edge[1]

            # ab i cd na ad i bc

            self.content[a].remove(b)
            self.content[b].remove(a)
            self.content[c].remove(d)
            self.content[d].remove(c)

            self.content[a].append(d)
            self.content[d].append(a)
            self.content[b].append(c)
            self.content[c].append(b)

    def __get_random_edges(self) -> list:
        edges: list = []

        while len(edges) < 4:
            edge_prep = self.__get_random_edge()
            if edge_prep[0] is not None and edge_prep[1] is not None: 
                edge = tuple(sorted(edge_prep))
            
                first_ver = edge[0]
                second_ver = edge[1]

                if first_ver not in edges and second_ver not in edges:
                    edges.append(first_ver)
                    edges.append(second_ver)

        edges = [(edges[0], edges[1]), (edges[2], edges[3])]
        return edges

    def __get_random_edge(self) -> tuple:
        first_ver = None
        second_ver = None
        if self.type is GraphTypes.AdjacencyList:
            first_ver = randint(1, len(self.content))

            if len(self.content[first_ver]) > 0:
                 second_ver = self.content[first_ver][randint(0, len(self.content[first_ver]) - 1)]

        return (first_ver, second_ver)

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