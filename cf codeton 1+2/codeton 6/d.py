for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    minm=min(arr)
    for i in range(n-1,-1,-1):
            if arr[i]==minm:
                index=i 
                break

    if k%minm==0:
        ans=[k//minm]*(index+1)
        ans.extend([0]*(n-index-1))
        print(*ans)
    else: 
        arrnew=[[minm,index]]
        for i in range(index+1,n):
            if arr[i]>arrnew[-1][0]:
                arrnew.append([arr[i],i])
        final=[]
        
        for i in range(len(arrnew)):
            #base
            if k==0:
                break
            ele=arrnew[i][0]
            times=k//ele
         
            rem=k%ele
        
            if len(final)==0:
                final.append(times)
                k=rem
                continue
            else:
                numprev=k//(ele-arrnew[i-1][0])
                numprev=min(numprev,final[-1])
                if numprev==0:
                    break
                final[-1]-=numprev
                times=(k+ (arrnew[i-1][0]*numprev))//ele
                final.append(times)
                k=(k+ (arrnew[i-1][0]*numprev))%ele

        newf=[]
        s=0
        final.reverse()
        for ele in final:
            s+=ele
            newf.append(s)
        indexes=[]
        newf.reverse()
        for i in range(len(final)):
            index=arrnew[i][1]
            indexes.append(index)
        
        # print(newf)
        # print(indexes)
        
        if len(newf)>0:
            ans=[newf[0]]*(indexes[0]+1)
            ans.extend([0]*(n-indexes[0]-1))
            for i in range(1,len(newf)):
                for j in range(indexes[i-1]+1,indexes[i]+1):
                    ans[j]=newf[i]
            print(*ans)

        else:
            print(*[0 for _ in range(n)])



        




            