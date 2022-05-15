from collections import defaultdict

def components_r(nr: int, v: int, adj_list: dict, comp: list):
    for u in adj_list[v]:
        if comp[u-1] == -1:
            comp[u-1] = nr
            components_r(nr, u, adj_list, comp)


def components(adj_list: dict):
    nr = 0

    comp:list = []
    for i in range(0, len(adj_list)):
        comp.append(-1)

    for v in adj_list.keys():
        if comp[v - 1] == - 1:
            nr = nr + 1
            comp[v - 1] = nr
            components_r(nr, v, adj_list, comp)

    return comp

def comp_to_string(comp:list, adj_list:dict):
    result = ''

    comp_number:dict = defaultdict(int)
    comp_vertices:dict = defaultdict(list)

    for c in comp:
        if c in comp_number:
            comp_number[c] = comp_number[c] + 1
        else:
            comp_number[c] = 1

    for key in comp_number:
        comp_vertices[key] = []

    for v in adj_list:
        comp_vertices[comp[v - 1]].append(v)

    for key in comp_vertices.keys():
        vertices = comp_vertices[key]

        result += str(key) + ')'
        for v in vertices:
            result += ' ' + str(v)
        
        result += '\n'

    return result

def find_biggest_comp(comp: list):
    comp_number:dict = defaultdict(int)

    for c in comp:
        if c in comp_number:
            comp_number[c] = comp_number[c] + 1
        else:
            comp_number[c] = 1

    biggest_comp_number: int = 0
    biggest_comp_size: int = 0

    for key in comp_number.keys():
        if comp_number[key] > biggest_comp_size:
            biggest_comp_size = comp_number[key]
            biggest_comp_number = key

    return biggest_comp_number