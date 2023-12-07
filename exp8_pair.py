def floydWarshall(graph):
    V = len(graph)
    dist = [[0 if i == j else INF for j in range(V)] for i in range(V)]

    for i in range(V):
        for j in range(V):
            if i != j:
                input_distance = input(f"Enter distance from vertex {i} to {j} (or 'INF' if no direct edge): ")
                if input_distance == 'INF':
                    graph[i][j] = INF
                else:
                    distance = int(input_distance)
                    graph[i][j] = distance

    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

V = int(input("Enter the number of vertices: "))

INF = float('inf')
graph = [[INF for _ in range(V)] for _ in range(V)]

shortest_distances = floydWarshall(graph)

print("Shortest distances between all pairs of vertices:")
for i in range(V):
    for j in range(V):
        if shortest_distances[i][j] == INF:
            print("INF", end="\t")
        else:
            print(shortest_distances[i][j], end="\t")
    print()
