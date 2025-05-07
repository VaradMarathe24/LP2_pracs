# Kruskal's Algorithm for Minimum Spanning Tree

# Helper function: Find parent with path compression
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

# Helper function: Union of two subsets
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Main Kruskal function
def kruskal_mst(graph, V):
    # Sort all edges by increasing weight
    edges = sorted(graph, key=lambda x: x[2])

    parent = [i for i in range(V)]
    rank = [0] * V

    mst = []  # Store MST edges

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:  # If including this edge doesn't form a cycle
            mst.append((u, v, weight))
            union(parent, rank, root_u, root_v)

    return mst

# ---------- Example ---------- #
if __name__ == "__main__":
    # (u, v, weight)
    graph = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    V = 4  # Number of vertices


    mst = kruskal_mst(graph, V)

    print("Edges in the Minimum Spanning Tree:")
    total_cost = 0
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
        total_cost += weight
    print(f"Total cost of MST: {total_cost}")


'''Edges in the Minimum Spanning Tree:
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Total cost of MST: 19'''
