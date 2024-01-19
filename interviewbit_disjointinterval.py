
def solve( arr):
    if len(arr)==1:
        return 1
    arr.sort()
    minm=arr[0][0]
    maxm=arr[0][1]
    c=1
    for i in range(1,len(arr)):
        if arr[i][0]<=maxm:
            if arr[i][1]<maxm:
                minm=arr[i][0]
                maxm=arr[i][1]
        else:
            c+=1
            minm=arr[i][0]
            maxm=arr[i][1]
    return c

print(solve([[3,5],[11,15]]))