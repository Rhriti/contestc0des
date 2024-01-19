arr=[]
for _ in range(int(input())):
    ww,xx=map(int,input().split())
    arr.append([xx,ww])
arr.sort()

maxm=0
for i in range(len(arr)-1):
    start=arr[i][0]
    lmax=arr[i][1]
    for j in range(i+1,len(arr)):
        if arr[j][0]-start>9:
            break
        lmax+=arr[j][1]
    maxm=max(maxm,lmax)
print('ans',maxm)

