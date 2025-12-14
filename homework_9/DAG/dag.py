def detect_cycle_and_toposort(graph):
    state = {node: 0 for node in graph}
    path = [] 
    def dfs(node):
        state[node] = 1
        path.append(node)
        
        for neighbor in graph.get(node, []):
            if state[neighbor] == 0:
                cycle = dfs(neighbor)
                if cycle:
                    return cycle
            elif state[neighbor] == 1:
                cycle_start_idx = path.index(neighbor)
                cycle = path[cycle_start_idx:] + [neighbor]
                return cycle
        
        path.pop()
        state[node] = 2
        return None
    
    for node in graph:
        if state[node] == 0:
            cycle = dfs(node)
            if cycle:
                return True, cycle
    
    topo_order = []
    visited = set()
    
    def topo_dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                topo_dfs(neighbor)
        topo_order.append(node)
    
    for node in graph:
        if node not in visited:
            topo_dfs(node)
    
    topo_order.reverse()
    return False, topo_order