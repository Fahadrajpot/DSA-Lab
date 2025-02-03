from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
  
    q = deque() # Create a queue for BFS

    # Mark the source node as visited and enqueue it
    if visited[s] == True:
        q.append(s)

    # Iterate over the queue
    while q:
        curr = q.popleft() # Dequeue a vertex
        print(curr, end=" ")

        # Get all adjacent vertices of curr
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True # Mark as visited
                q.append(x) # Enqueue it

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u) # Undirected graph

# Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj) # Not visited

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)

# Example usage
V = 6 # Number of vertices
adj = [[] for _ in range(V)] # Adjacency list

# Add edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)

# Perform BFS traversal for the entire graph
bfs(adj)