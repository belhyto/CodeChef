graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [5],
    4: [5],
    5: [6],
    6: []
}

start_node = 0
visited = set()
stack = [start_node]

while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

print("DFS visited nodes:", visited)
