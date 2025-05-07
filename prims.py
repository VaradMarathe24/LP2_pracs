def prims_simple(graph):
    n = len(graph)
    selected = [False] * n
    key = [float('inf')] * n
    parent = [-1] * n

    key[0] = 0  # Start from node 0

    for _ in range(n):
        # Find the minimum key vertex not yet in MST
        min_val = float('inf')
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_val:
                min_val = key[v]
                u = v

        selected[u] = True

        # Update adjacent vertices
        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print MST
    print("Minimum Spanning Tree:")
    cost = 0
    for i in range(1, n):
        print(f"{parent[i]} - {i}  weight: {graph[i][parent[i]]}")
        cost += graph[i][parent[i]]
    print("Total cost:", cost)

# Sample graph (undirected and weighted)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims_simple(graph)
