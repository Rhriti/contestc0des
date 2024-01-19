for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
   
    #negeative jodd ke ek kardo guys
    count=0
    dnew=[0]
    for ele in d:
        if ele<0:
            count+=ele
            continue
        else:
            if count==0:
                dnew.append(ele)
                continue
            else:
                dnew.append(count)
                count=0
                dnew.append(ele)
    if count!=0:
        dnew.append(count)


    minm=min(dnew)
    if  minm>=0:
        print(0)
    else:
        index=dnew.index(minm)
        ans=sum(dnew[:index])
        if ans<0:
            print(0)
        else:
            print(ans)