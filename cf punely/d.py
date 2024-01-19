for _ in range(int(input())):
    lef,ri=map(int,input().split())
    g=[]
    for _ in range(lef):
        s=input()
        t=[]
        for ele in s:
            t.append(ele)
        g.append(t)
    row=[0]*len(g)
    col=[0]*len(g[0])
    for r in range(len(g)):
        count=0
        for c in range(len(g[0])):
            if g[r][c]=='L' or g[r][c]=='U' or g[r][c]=='D' or g[r][c]=='R':
                count+=1
                col[c]+=1
        row[r]=count
    f=False
    for ele in row:
        if ele%2==1:
            f=True
            break
    for ele in col:
        if ele%2==1:
            f=True
            break
    if f:
        print(-1)
    else:
        for r in range(len(g)):
            for c in range(len(g[0])):
                if g[r][c]=='L':
                    g[r][c]='B'
                    g[r][c+1]='W'
                    row[r]-=2
                    col[c]-=1
                    col[c+1]-=1
        for r in range(len(g)):
            bl=1
            for c in range(len(g[0])):
                if g[r][c]=='U':
                    if bl<=row[r]//2:
                        bl+=1
                        g[r][c]='B'
                        g[r+1][c]='W'
                    else:
                        g[r][c]='W'
                        g[r+1][c]='B'
                    row[r]-=1
                    row[r+1]-=1
                    
        for r in range(len(g)):
            for c in range(len(g[0])):
                print(g[r][c],end='')
            print()
    

            
