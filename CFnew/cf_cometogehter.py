#a,b,c teeno hi faltu question the 
import math
for _ in range(int(input())):
    ax,ay=map(int,input().split())
    bx,by=map(int,input().split())
    cx,cy=map(int,input().split())
    d1=[cx,by]
    d2=[bx,cy]
    vertex=[[cx,cy],[bx,by],d1,d2]
    

    def dist(v): #(vertrex,point)
        dis=((v[0]-ax)**2) + ((v[1]-ay)**2)
        return dis
    if min(bx,cx)<=ax<=max(cx,bx) and min(by,cy)<=ay<=max(cy,by):
        if by==cy:
            print(abs(by-ay)+1)
        elif bx==cx:
            print(abs(ax-bx)+1)
        else:
            print(1)

    elif min(bx,cx)<=ax<=max(cx,bx) or min(by,cy)<=ay<=max(cy,by):
        if min(bx,cx)<=ax<=max(cx,bx) and not min(by,cy)<=ay<=max(cy,by):
            if ay<cy and ay<by:
                print(min(by,cy)-ay+1)
            else:
                print(ay-max(by,cy)+1)
        else:
            if ax<cx and ax<bx:
                print(min(cx,bx)-ax+1)
            else:
                print(ax-max(cx,bx)+1)
    else:
        minm=float('inf')
        for ele in vertex:
            dis=dist(ele)
            # print(f'{ele} ka distane a se {dis}')
            if dis<minm:
                minm=dis
                # print(f'vx {ele[0]}  vy {ele[1]}')
                ans=abs(ax-ele[0])+abs(ay-ele[1])+1
        print(ans)




        