
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if len(arr)==1:
        print('NO')
    else:
        count1=0
        sums=sum(arr)
        for ele in arr:
            if ele==1:
                count1+=1
                sums-=2
        left=len(arr)-count1
        if sums>=left:
            print('YES')
        else:
            print('NO')

    