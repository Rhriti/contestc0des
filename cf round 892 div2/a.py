from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    g=Counter(arr)
    if len(g)==1:
        print(-1)
    else:
        big=max(g.keys())
        b=[]
        c=[]
        for ele in arr:
            if ele==big:
                c.append(ele)
            else:
                b.append(ele)
        print(f'{len(b)} {len(c)}')
        for ele in b:
            print(ele,end=' ')
        print()
        for ele in c:
            print(ele,end=' ')
        print()
        print('upar')
        