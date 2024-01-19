for _ in range(int(input())):
    n=int(input())
    pres=[]
    s=0
    for i in range(1,n+1):
        s+=i*i
        pres.append(s)
    maxm=float('-inf')
    reverse=n
    rsums=0
    rmax=float('-inf')
    for i in range(n):
        rsums+=(i+1)*reverse
        rmax=max(rmax,(i+1)*reverse)
        reverse-=1
        ps=pres[i]
        t=i+2
        lmax=(i+1)*(i+1)
        for j in range(n,i+1,-1):
            ps+=j*t
            lmax=max(lmax,j*t)
            t+=1
        maxm=max(maxm,ps-lmax)
    print(max(maxm,rsums-rmax))
   
    #pura reverse

        
