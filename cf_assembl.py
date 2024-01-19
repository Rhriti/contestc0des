from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    g=Counter(s)
    nums=[ele for ele in g.keys()]
    nums.sort()
    arr=[None for _ in range(n)]
    i=0
    for ele in nums:
        while g[ele]!=0:
            count=n-1-i
            g[ele]-=count
            arr[i]=ele
            i+=1
    if i ==n-1:
        arr[i]=nums[-1]
    for ele in arr:
        print(ele,end =' ')
    print()


