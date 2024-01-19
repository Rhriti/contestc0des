from collections import defaultdict

def maxKDivisibleComponents( n , edges , values , k ):
    g=defaultdict(list)
    st=set(ele for ele in range(n))
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
        
    gnew=defaultdict(list)
    visit=set()
    par={0:0}
    def t(node):
        visit.add(node)
        for ch in g[node]:
            if ch not in visit:
                par[ch]=node
                gnew[node].append(ch)
                t(ch)
    t(0)
    g=gnew
    # print(par)
    outd={ele:0 for ele in range(n)}
    for keys in g.keys():
        st.remove(keys)
        outd[keys]+=len(g[keys])
    st=list(st)
    # print(outd)
    c=0
    while st:
        out=st.pop()
        if out==0:
            if values[0]%k==0:
                c+=1
            break
        if values[out]%k==0:
            c+=1
            outd[par[out]]-=1
            if outd[par[out]]<=0:
                st.append(par[out])
                del outd[par[out]]
        else:
            values[par[out]]+=values[out]
            outd[par[out]]-=1
            if outd[par[out]]<=0:
                st.append(par[out])
                del outd[par[out]]
    return c
                

print(maxKDivisibleComponents(1,
[],
[0],
1))