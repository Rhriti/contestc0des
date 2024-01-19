n,l,r=map(int,input().split())
arr=list(map(int,input().split()))
final=[]
for ele in arr:
  if ele<l:final.append(l)
  elif ele>r:final.append(r)
  else:final.append(ele)

print(*final)