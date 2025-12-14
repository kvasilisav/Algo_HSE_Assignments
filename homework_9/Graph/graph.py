def find_connected_components(graph):
    if not graph:
        return []
    
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for node in graph.keys():
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)
    
    return components