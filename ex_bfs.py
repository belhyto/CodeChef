from collections import deque

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
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

print("BFS visited nodes:", visited)
