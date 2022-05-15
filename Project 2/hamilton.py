def get_path_hamilton(adj_list: dict):
    start_vertex = 1
    path = []

    is_hamiltion = check_if_hamiltonian(adj_list, start_vertex, path)
    
    if is_hamiltion:
        return path
    else: 
        return None

def check_if_hamiltonian(adj_list: dict, vertex: int, path: list):
    path.append(vertex)
    is_hamilton = False

    # Adding starting vertex at the and of path
    if len(path) == len(adj_list.keys()):
        path.append(path[0])
        return True

    for v in adj_list[vertex]:
        if v not in path:
            is_hamilton = check_if_hamiltonian(adj_list, v, path)

    if is_hamilton:
        return True
    path.pop(-1)