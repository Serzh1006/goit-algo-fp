import heapq

def create_graph(edges):
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3)
    ]
    
    graph = create_graph(edges)
    
    start_vertex = 'A'
    
    distances = dijkstra(graph, start_vertex)
    
    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Відстань до {vertex}: {distance}")


if __name__ == "__main__":
    main()