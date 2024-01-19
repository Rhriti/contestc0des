import copy 
for _ in range(int(input())):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    x-=1
    y-=1
    if n%2==0 :
        if x==n//2 and y==m//2:
            i,j=x-1,y
        else:i,j=n//2,m//2
        
    elif m%2==0:
        if x==n//2 and y==m//2:
            i,j=x,y-1
        else:
            i,j=n//2,m//2
    else:
        if x==n//2 and y==m//2:
            i,j=(n//2)-1,m//2
        else:i,j=n//2,m//2


    green={(i,j)}
    gst=[[i,j]]
    red={(x,y)}
    rst=[[x,y]]
    cg=1
    print('i,j',i,j)

    while len(red)+len(green)!=n*m:
        
        while rst:
            t=[]
            while rst:
                xnew,ynew=rst.pop()
                for dx,dy in [[xnew+1,ynew],[xnew-1,ynew],[xnew,ynew+1],[xnew,ynew-1]]:
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in green and (dx,dy) not in red:
                        red.add((dx,dy))
                        t.append([dx,dy])
        rst=t

        
        while gst:
            t2=[]
            while gst:
                xnew,ynew=gst.pop()
                for dx,dy in [[xnew+1,ynew],[xnew-1,ynew],[xnew,ynew+1],[xnew,ynew-1]]:
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in green and (dx,dy) not in red:
                        green.add((dx,dy))
                        cg+=1
                        t2.append([dx,dy])
        gst=t2

    print('ans',cg)
