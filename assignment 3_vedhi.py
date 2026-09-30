# Kruskal's Algorithm - Minimum Spanning Tree

# Number of vertices and edges
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

# Store edges as (weight, vertex1, vertex2)
edges = []

print("Enter edges (source destination weight):")

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges according to weight
edges.sort()

# Parent array for checking cycles
parent = []
for i in range(n):
    parent.append(i)

mst = []
total_cost = 0

# Find parent of a vertex
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

# Kruskal's Algorithm
for w, u, v in edges:

    parent_u = find(u)
    parent_v = find(v)

    # If parents are different, adding edge will not create a cycle
    if parent_u != parent_v:

        mst.append((u, v, w))
        total_cost += w

        # Join the two sets
        parent[parent_v] = parent_u

# Display MST
print("\nEdges in Minimum Spanning Tree:")

for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Minimum Cost =", total_cost)