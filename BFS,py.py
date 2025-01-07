from collections import deque

def bfs(adj, s):

    queue = deque()
    visited = [False] * len(adj)

    queue.append(s)
    visited[s] = True

    while queue:
        curr = queue.popleft()
        print(curr, end = " ")

        for x in range(len(adj[curr])) :
            if not visited[x]:
                queue.append(adj[curr][x])
                visited[x] = True

def add_edge(adj, u ,v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":

    V = 5
    adj = [[] for _ in range(V)]

    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 2, 3)

bfs(adj,0)

