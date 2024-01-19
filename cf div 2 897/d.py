import sys
for _ in range(int(input())):
    n,k=map(int,input().split())
    sys.setrecursionlimit(n+1)
    arr = [x for x in map(int, input().split())]
    if k==1:
        if arr==list(range(n)):
            print('YES')
        else:
            print('NO')
    else:
        memo={}
        def dfs(node,c):
            if node in memo:
                return memo[node]

            count[node]=c
            ch=arr[node]
            if count[ch] is None:
                local=dfs(ch,c+1)
            else:
                if abs(count[node]-count[ch])+1==k:
                    local=True
                else:
                    local= False
            memo[node]=local
            return local
            
        final='YES'
        for i in range(1,n+1):
            count=[None for _ in range(n+1)]
            ans=dfs(i,0)
            if ans is False:
                final='NO'
                break
        print(final)