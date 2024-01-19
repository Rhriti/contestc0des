import bisect
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    pos=[]
    f=False
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            f=True
            #dec hai
        if arr[i]>0:
            pos.append([arr[i],i])
    if arr[-1]>0:
        pos.append([arr[-1],len(arr)-1])
    pos.sort()

    st=[arr[0]]
    order=[]
    for i in range(1,len(arr)):  #i me add kre
        if arr[i]>=st[-1]:
            st.append(arr[i])
        else:
            req=st[-1]-arr[i]
            # index=bisect.bisect_left(pos,req)
            index=len(pos)-1
            for t in range(len(pos)):
                if pos[t][0]>=req:
                    index=t
                    break
            if index==0:
                order.append([i,pos[0][1]])
                st.append(arr[i]+pos[0][0])
                continue
               
            print(f'req {req}')
            print(pos)
            print(index)
            if index<len(pos) and pos[index][1]==req:
                order.append([i+1,pos[-1][1]])
                st.append(st[-1])
            else:
                news=arr[i]
                for j in range(index-1,-1,-1):
                    #base
                    if req<pos[j][0]:
                        last=pos[j][0]
                        index2=j
                        for k in range(j-1,-1,-1):
                            if pos[k]>=req:
                                last=min(last,pos[k][0])
                                index2=k
                        news+=pos[index2][0]
                        order.append([i+1,pos[index2][1]+1])

                    times=req//pos[j][0]
                    for _ in range(times):
                        order.append([i+1,pos[j][1]+1])
                    req=req-(times*pos[j][0])
                    news+=times*pos[j][0]
                st.append(news)
    
    print(len(order))
    for ele in order:
        print(ele[0],end=' ')
        print(ele[1])
    print()


