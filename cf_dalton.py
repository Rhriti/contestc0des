for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    c=0
    for i in range(1,n+1):
        if i==s[i-1]:
            c+=1
    if c%2==0:
        print(c//2)
    else:
        print((c//2)+1)
    