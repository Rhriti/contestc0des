for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    f=False
    pos=[]
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            f=True
        if arr[i]>0:
            pos.append([arr[i],i])
    if arr[-1]>0:
        pos.append([arr[-1],n-1])
    pos.sort()
    if not f:
        print(0)
    elif f and len(pos)==0:
        print(0)
    else:
        prev=arr[0]
        order=[]
        
        for i in range(1,n):
            if arr[i]>=prev:
                prev=arr[i]
            else:
                req=prev-arr[i]
                if pos[0][0]>=req:
                    index=0  
                    prev=arr[i]+pos[0][0]
                    arr[i]=prev
                    order.append([i,pos[0][1]])
                    if prev>0:
                        pos.append([prev,i])
                    pos.sort()
                    #all done here
                else:
                    index=len(pos)-1
                    for j in range(1,len(pos)):
                        if pos[j][0]>req:
                            index=j-1
                            break
                    for k in range(index,-1,-1):
                        times=req//pos[k][0]
                        if times==0:
                            for p in range(k+1):
                                if pos[p][0]>=req:
                                    newi=p
                                    break
                            prev=prev+(pos[newi][0]-req)
                            arr[i]=prev
                            if prev>0:
                                pos.append([prev,i])
                            pos.sort()
                            order.append([i,pos[newi][1]])
                            break


                        for _ in range(times):
                            order.append([i,pos[k][1]])
                        req-=times*pos[k][0]
                        #important base case
                        if req==0:
                            break
        
        print(len(order))
        for ele in order:
            print(ele[0]+1,end=' ')
            print(ele[1]+1)
        print()
                    
                



        