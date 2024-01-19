for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    ans=[]
    dnew=[]
    if n==1:
        print(1)
    else:
        ans.append(1)
        dnew.append(d[0])
        dip=False
        for i in range(1,n):
            #dip true ka alag se dekhenge
            if dip:
                if d[i]<=d[0] and d[i]>=dnew[-1]:
                    ans.append(1)
                    dnew.append(d[i])
                else:
                    ans.append(0)
            else:
                if d[i]>=dnew[-1]:
                    ans.append(1)
                    dnew.append(d[i])
                else:
                    if d[i]<=d[0]:
                        dip=True
                        ans.append(1)
                        dnew.append(d[i])
                    else:
                        ans.append(0)
        for ele in ans:
            print(ele,end='')
        print()

                


            
            
