from tracemalloc import start
import numpy as np

class Generator:
    @staticmethod
    def generate_nl(n: int, l: int) -> np.ndarray:
        vertices_number = n
        edges_number = l
        generated_edges = 0
        incidence_matrix: np.ndarray = np.zeros((vertices_number, edges_number), int)

        if edges_number > int(vertices_number * (vertices_number - 1) / (2)):
            return incidence_matrix

        incidence_matrix: np.ndarray = np.zeros((vertices_number, edges_number), int)

        edges_list: list = []

        while generated_edges < edges_number:
            start_edge, end_edge = np.random.choice(range(vertices_number), size=2)
            edge = (start_edge, end_edge)
            reversed_edge = (end_edge, start_edge)
            if (edge not in edges_list) and (reversed_edge not in edges_list) and (start_edge != end_edge):
                generated_edges = generated_edges + 1
                edges_list.append(edge)

        for i in range(0, len(edges_list)):
            edge = edges_list[i]
            incidence_matrix[edge[0]][i] = 1
            incidence_matrix[edge[1]][i] = 1

        return incidence_matrix

    @staticmethod
    def generate_np(n: int, p: int) -> np.ndarray:
        vertices_number = n
        edge_probability = p
        generated_edges = 0

        if edge_probability < 0 or edge_probability > 1:
            incidence_matrix: np.ndarray = np.zeros((vertices_number, vertices_number), int)
            return incidence_matrix

        edges_list: list = []

        for i in range(0, vertices_number):
            for j in range(i+1, vertices_number):
                random_number = np.random.uniform(0, 1)
                if random_number < edge_probability:
                    generated_edges = generated_edges + 1
                    edge = (i, j)
                    edges_list.append(edge)
        
        incidence_matrix: np.ndarray = np.zeros((vertices_number, generated_edges), int)

        for i in range(0, len(edges_list)):
            edge = edges_list[i]
            incidence_matrix[edge[0]][i] = 1
            incidence_matrix[edge[1]][i] = 1
        
        return incidence_matrix
            