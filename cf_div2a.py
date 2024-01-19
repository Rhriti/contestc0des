for _ in range(int(input())):
    b,c,h=map(int,input().split())
    c+=h
    if b==c:
        print(b+b-1)
    if b>c:
        print(c+c+1)
    if c>b:
        print(b+b-1)
    