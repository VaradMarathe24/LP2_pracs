def prims_simple(graph):
    n = len(graph)
    selected = [False] * n          # Track vertices included in MST
    key = [float('inf')] * n        # Key values used to pick minimum weight edge
    parent = [-1] * n               # Array to store constructed MST
    total_comparisons = 0           # Count the number of comparisons made

    key[0] = 0  # Start from vertex 0

    print("\nPrim's Algorithm Execution:\n")

    # Loop to construct MST with n vertices
    for step in range(n):
        min_val = float('inf')
        u = -1

        # Step 1: Pick the minimum key vertex from set of vertices not yet in MST
        for v in range(n):
            total_comparisons += 1
            if not selected[v] and key[v] < min_val:
                min_val = key[v]
                u = v

        selected[u] = True
        print(f"Step {step+1}: Selected vertex {u} with key {min_val}")

        # Step 2: Update key and parent of adjacent vertices
        for v in range(n):
            # Update the key only if graph[u][v] is smaller and v is not yet selected
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Step 3: Output the MST edges and total cost
    print("\nMinimum Spanning Tree (MST):")
    cost = 0
    mst_edges = []
    for i in range(1, n):
        print(f"{parent[i]} - {i}  weight: {graph[i][parent[i]]}")
        mst_edges.append((parent[i], i, graph[i][parent[i]]))
        cost += graph[i][parent[i]]

    print("\nEdge List Format (for visualization):")
    for u, v, w in mst_edges:
        print(f"({u}, {v}) -> weight: {w}")

    print(f"\nTotal cost of MST: {cost}")
    print(f"Total comparisons made during selection: {total_comparisons}")
