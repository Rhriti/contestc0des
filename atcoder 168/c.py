from collections import Counter
n,k=map(int,input().split())
s=input()
g=Counter(s)
count=0

t=g['A']*g['B']
count+=t
# if t<=k:
#     k-=t
#     count+=t
# else:
#     count+=k
#     k=0

t=g['B']*g['C']
count+=t
# if t<=k:
#     k-=t
#     count+=t
# else:
#     count+=k
#     k=0

t=g['A']*g['C']
count+=t
# if t<=k:
#     k-=t
#     count+=t
# else:
#     count+=k
#     k=0
count=k*count
count+=1

print(count)