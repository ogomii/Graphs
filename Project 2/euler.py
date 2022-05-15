from random import randrange
from Converter import Converter 

def generate_random_euler_graph(vertices_amount: int):
    sequence:list = []
    
    while True:
        sequence = []

        for i in range(0, vertices_amount // 2):
            sequence.append(randrange(2, vertices_amount, 2))
        
        sequence = sequence * 2

        if len(sequence) == vertices_amount - 1:
            sequence.append(randrange(2, vertices_amount, 2))

        if is_sequence(sequence.copy()):
            return Converter.sequence_to_adj_list(sequence)

def get_euler_cycle(adj_list: dict):
    return []
      

def get_edges_amount(adj_list: dict):
    edge_amount = 0

    for v in adj_list.keys():
        for n in adj_list[v]:
            edge_amount += 1
    return edge_amount / 2

def is_sequence(a: list):
    while True:
        a.sort(reverse=True)
       
        only_zeros = True
        for element in a:
            if not element == 0:
                only_zeros = False

        if only_zeros:
            return True 
        
        if a[0] < 0 or a[0] > len(a):
            return False
        
        for element in a:
            if element < 0:
                return False

        for i in range(1, a[0] + 1):
            a[i] = a[i] - 1
        a[0] = 0
 
