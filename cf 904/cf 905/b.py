from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    g=Counter(input())
    odd_count = sum(1 for value in g.values() if value % 2 != 0)
    if k>=odd_count-1:
        print('YES')
    else:
        print('NO')


