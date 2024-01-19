for _ in range(int(input())):
    n=int(input())
    k=[[0 for _ in range(n)] for _ in range(n)]
    g=[[] for _ in range(n)]
    for i in range(n):
        s=input()
        for ele in s:
            g[i].append(int(ele))
    print(g)
    ans=0
    for r in range(len(g)):
        cnow=0
        for c in range(len(g[0])):
            cnow+=k[r][c]
            g[r][c]=(g[r][c]+cnow)%2
            # if g[r][c]==1:
            #     g[r][c]=0
            #     x1,y1=r+1,c-1
            #     x2,y2=r+1,c+2
            #     if 0<=x1<len(g) and 0<=y1<len(g[0]): 
            #         k[x1][y1]+=1
            #     if 0<=x2<len(g) and 0<=y2<len(g[0]):
            #         k[x2][y2]-=1
            #     if 0<=x1<len(g) and y2<0:
            #         k[x1][0]+=1

    print('ans',ans)
        

    