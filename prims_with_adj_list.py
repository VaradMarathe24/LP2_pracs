import heapq

def prims_with_adj_list(adj_list, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    parent = [-1] * n
    key = [float('inf')] * n
    key[0] = 0
    total_cost = 0
    total_comparisons = 0

    print("\nPrim's Algorithm (Adjacency List Version):\n")

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight
        print(f"Selected Vertex: {u} with Edge Weight: {weight}")

        for v, w in adj_list[u]:
            total_comparisons += 1
            if not visited[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(min_heap, (w, v))

    print("\nMinimum Spanning Tree:")
    for i in range(1, n):
        print(f"{parent[i]} - {i}  weight: {key[i]}")
    print(f"\nTotal Cost of MST: {total_cost}")
    print(f"Total comparisons made: {total_comparisons}")


# Sample adjacency list (undirected, weighted)
adj_list = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

# Convert dict to list of lists for consistency
n = len(adj_list)
adj_list_ordered = [[] for _ in range(n)]
for u in adj_list:
    adj_list_ordered[u] = adj_list[u]

# Run the algorithm
prims_with_adj_list(adj_list_ordered, n)
