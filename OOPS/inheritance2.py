for _ in range(int(input())):
    r,c=map(int,input().split())
    g=[]
    for _ in range(r):
        t=input()
        g.append(t)
    arr=['v','i','k','a']
    i=0
    for col in range(c):
        for row in range(r):
            #base
            if i==4:
                break
            if g[row][col]==arr[i]:
                i+=1
                break
        if i==4:
            break
    
    if i==4:
        print('YES')
    else:
        print('NO')
