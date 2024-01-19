from collections import defaultdict,deque

n=int(input())
s=list(input().split())
g1={}
arr=[[],[],[],[],[],[]]
for ele in s:arr[len(ele)].append(ele)
g1={1:defaultdict(int),2:defaultdict(int),3:defaultdict(int),4:defaultdict(int),5:defaultdict(int)}
def sums(st):
    s=0
    for ele in st:s+=int(ele)
    return s

for ele in s:g1[len(ele)][sums(ele)]+=1
g2={1:{1:defaultdict(int)},2:{1:defaultdict(int),2:defaultdict(int)},3:{1:defaultdict(int),2:defaultdict(int),3:defaultdict(int)},
4:{1:defaultdict(int),2:defaultdict(int),3:defaultdict(int),4:defaultdict(int)},5:{1:defaultdict(int),2:defaultdict(int),3:defaultdict(int),
4:defaultdict(int),5:defaultdict(int)}}
for ele in s:
    t=deque()
    s=0
    for j in range(len(ele)-1,-1,-1):
        s+=int(ele[j])
        t.appendleft(s)
    k=1
    while t:
        out=t.pop()
        g2[len(ele)][k][out]+=1
        k+=1
    

