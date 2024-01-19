for _ in range(int(input())):
    m,k,a1,ak=map(int,input().split())
    reach=k*ak
    if reach==m:
        print(0)
    else:
        if reach<m:
            index=ak*k
            left=m-index
            if left-a1<=0:
                print(0)
            else:
                if left<k:
                    way1=left-a1
                    if way1<=0:
                        print(0)
                    else:
                        print(way1)
                else:
                    # rem=left%k
                    # now=(left//k)+rem
                    # for ele in range(1,a1+1):
                    #     newindex=index+ele
                    #     left=m-newindex
                    #     rem=left%k
                    #     now=min(now,(left//k)+rem)
                    # print(now)
                    reach=index+a1
                    now=float('inf')
                    for newreach in range(reach,index-1,-1):
                        left=m-newreach
                        rem=left%k
                        if rem+(left//k)<now:
                            now=rem+(left//k)


        else:
            index=k*(m//k)
            left=m-index
            left-=a1
            if left<=0:
                print(0)
            else:
                print(left)
