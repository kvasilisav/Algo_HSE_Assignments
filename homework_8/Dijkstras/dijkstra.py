import heapq

def dijkstra(graph, start):
    dist = {vertex: float('infinity') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_dist > dist[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    return dist, prev

def get_shortest_path(prev, target):
    path = []
    vertex = target
    
    while vertex is not None:
        path.append(vertex)
        vertex = prev[vertex]
    
    path.reverse()
    return path