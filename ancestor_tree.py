#how to find if a node is ancestor of another node in O(1) itme
g = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7, 8],
    5: [2],
    6: [2],
    7: [4],
    8: [4]
}
en={}
ex={}
count=[0]
v=set()
def dfs(node):
    v.add(node)
    en[node]=count[0]
    count[0]+=1
    for ch in g[node]:
        if ch not in v:
            dfs(ch)
    ex[node]=count[0]
dfs(1)
print(en,ex)


