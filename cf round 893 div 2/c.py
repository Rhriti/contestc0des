for _ in range(int(input())):
    x=int(input())
    ans=[]
    s=set()
    for i in range(x,0,-1):
        if i in s:
            continue
        n=i
        ans.append(n)
        s.add(n)
        while n%2==0:
            ans.append(n//2)
            s.add(n//2)
            n=n//2
    for ele in ans:
        print(ele,end=' ')
    print()