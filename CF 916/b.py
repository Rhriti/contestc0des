for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[ele for ele in range(n,0,-1)]
    news=arr[:k+1][::-1]+arr[k+1:]
    print(*news)