for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>=n:
        if (n==1 and k==1) or (n==1 and k==2) or (n==2 and k==3) or(n==3 and k==5) or (n==5 and k==5):
            print(1)
        else:
            print(0)      
    else:
        mx={}
        my={}
        def fibx(index):
            if index==1 or index==2:
                return 1
            if index in mx:
                return mx[index]
            t=fibx(index-1)+fibx(index-2)
            mx[index]=t
            return t
        
        def fiby(index):
            if index in my:
                return my[index]
            if index==1:
                return 1
            if index==2:
                return 2
            t=fiby(index-1)+fiby(index-2)
            my[index]=t
            return t
        xlast=fibx(k-2)
        ylast=fiby(k-2)
        print(xlast)
        print(ylast)
        c=0
        for x in range(n+1):
            y=(n-(xlast*x))/ylast
            if y==int(y) and y>x:
                # print(x,y)
                c+=1
        print(c)
    print('upar ')


