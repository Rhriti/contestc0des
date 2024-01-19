from collections import defaultdict
def processLogs(logs,threshold):
    g=defaultdict(int)
    for ele in logs:
        s,r,amt=ele.split(' ')
        if s==r:
            g[s]+=1
        else:
            g[s]+=1
            g[r]+=1
    final=[]
    for k,v in g.items():
        if v>=threshold:
            final.append(int(k))
    final.sort()
    ans=[]
    for ele in final:
        ans.append(str(ele))
    return ans

print(processLogs(['88 99 200','88 99 300','99 32 100','12 12 15'],2))