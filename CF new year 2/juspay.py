from collections import defaultdict

def dfs(node, par):
    visited[node] = True
    for child in edge[node]:
        if not visited[child]:
            dfs(child, node)
    if par != -1:
        dirty[par] = dirty[par] or dirty[node]

if __name__ == "__main__":
    n = int(input())
    sz = 0
    for _ in range(n):
        node = int(input())
        sz = max(sz, node + 1)
   
    edge = defaultdict(list)
    visited = [False] * sz
    dirty = [False] * sz

    edges = int(input())
    for _ in range(edges):
        u, v = map(int, input().split())
        edge[v].append(u)

    enemy=int(input())
    person=int(input())
    dirty[enemy] = True
    dfs(person, -1)

    for child in edge[person]:
        if dirty[child]:
            print(child, end=" ")
