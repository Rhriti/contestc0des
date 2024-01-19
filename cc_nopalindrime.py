for _ in range(int(input())):
    n, k = map(int, input().split())
    L = 2 + k + ((k-1)//2)
    
    # (x-1)L + 1 <= N
    # (x-1)L <= N-1
    # x <= (N-1)/L + 1
    x = (n-1)//L + 1
    
    # k+2+(y-1)L <= N
    # y <= (N-k-2)/L + 1
    y = 0
    if n >= k+2: y = (n-k-2)//L + 1
    
    print(x + 2*y)