
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            else:
                self.parent[yr] = xr
                self.rank[xr] += 1

# def minimumSpanningTree(edges, V, E):
#     # uf = UnionFind(V)
#     # edges.sort(key=lambda edge: edge.weight)
#     # mst = []
#     # for edge in edges:
#     #     if uf.find(edge.start) != uf.find(edge.end):
#     #         uf.union(edge.start, edge.end)
#     #         mst.append(edge)
#     # return mst

