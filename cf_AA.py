for _ in range(int(input())):
    n=int(input())
    count=0
    for _ in range(n):
        a,b=map(int,input().split())
        if b<a:
            count+=1
    print(count)