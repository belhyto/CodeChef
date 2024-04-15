class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []

        self.adjacency_list[source].append(destination)

    def dfs(self, start_node):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        return visited


graph = Graph()
num_edges = int(input("Enter the number of edges: "))
for i in range(num_edges):
    source, destination = map(int, input(f"Enter edge {i + 1} (source destination): ").split())
    graph.add_edge(source, destination)

start_node = int(input("Enter the starting node for traversal: "))
visited_nodes_dfs = graph.dfs(start_node)
print("DFS visited nodes:", visited_nodes_dfs)

