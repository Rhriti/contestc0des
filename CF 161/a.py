for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    c=input()
    f=True
    for i in range(n):
        if a[i]!=b[i]!=c[i]:print('YES');f=False;break
        if a[i]==b[i]==c[i]:print('YES');f=False;break
    if f:print('NO')