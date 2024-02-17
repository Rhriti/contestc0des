for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    recent=[[i,i] for i in range(n)]
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            recent[i][0]=i-1
        else:
            if recent[i-1][0]!=recent[i-1][1]:
                recent[i][0]=recent[i-1][0]
    q=int(input())
    for _ in range(q):
        i,j=map(int,input().split())
        i-=1
        j-=1
        if arr[i]!=arr[j]:print(i+1,j+1)
        else:
            
            if recent[j][0]>=i and recent[j][0]!=recent[j][1]:print(recent[j][0]+1,recent[j][1]+1)
            else:print(-1,-1)
    # print('upar ans')