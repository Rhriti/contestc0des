for _ in range(int(input())):
    r,c,xa,ya,xb,yb=map(int,input().split())
    if xa>=xb:print('DRAW')
    else:
        ra=[ya,ya]
        rb=[yb,yb]
        count=0
        while xa<=xb:
            if count%2==0:
                ra[0]=max(1,ra[0]-1)
                ra[1]=min(c,ra[1]+1)
                xa+=1
            else:
                rb[0]=max(1,rb[0]-1)
                rb[1]=min(c,rb[1]+1)
                xb-=1
            if xa==xb:
                if count%2==0:
                    if ra[0]<=rb[0] and rb[1]<=ra[1]:print('Alice')
                    else:print('Draw');break
                else:
                    if rb[0]<=ra[0] and ra[1]<=rb[1]:print('Bob')
                    else:print('Draw');break
            
            count+=1
            
