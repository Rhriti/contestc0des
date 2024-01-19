#this seems like a dp problem but it ain't

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    st=[[arr[0],0]]
    maxl=1
    for i in range(1,n):
        if arr[i]<=st[-1][0]:
            st.append([arr[i],i])
        else:
            f=False
            while len(st)>1 and arr[i]>st[-1][0]:
                f=True
                st.pop()
            if f:
                st.append([arr[i],i])

        maxl=max(maxl,len(st))
    v=set()
    for ele in st:v.add(ele[1])

    curr=-100
    c=-1
    for i in range(n):
        if i not in v:
            if arr[i]>curr:
                curr=arr[i]
                c+=1
    

    print(c if c!=-1 else 0 )

    
            
