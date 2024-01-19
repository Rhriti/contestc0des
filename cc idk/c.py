from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    if n%2==0:
        ra=arr[(n//2):]
        r=Counter(ra)
        chalega=len(r)-2
        la=arr[:(n//2)]
        lmax=max(la)
        l=Counter(la)
        final=[]
        if lmax==arr[(n//2)+1]:
            if l[lmax]<=chalega:
                for i in range(len(ra)):
                    final.append(la[i])
                    final.append(ra[i])
                print(*final)
            else:
                print(-1)

        else:
            for i in range(len(ra)):
                final.append(la[i])
                final.append(ra[i])
            print(*final)

    else:
        ra=arr[(n//2)+1:]
        r=Counter(ra)
        chalega=len(r)-1
        la=arr[:(n//2)+1]
        lmax=max(la)
        l=Counter(la)
        final=[]
        if lmax==arr[(n//2)+1]:
            if l[lmax]<=chalega:
                for i in range(len(ra)):
                    final.append(la[i])
                    final.append(ra[i])
                final.append(la[-1])
                print(*final)
            else:
                ra=arr[(n//2):]
                r=Counter(ra)
                chalega=len(r)-2
                la=arr[:(n//2)]
                lmax=max(la)
                l=Counter(la)
                if lmax==arr[(n//2)+1]:
                    if l[lmax]<=chalega:
                        for i in range(len(la)):
                            final.append(ra[i])
                            final.append(la[i])
                        final.append(ra[-1])
                        print(*final)
                    else:
                        print(-1)

                else:
                    for i in range(len(la)):
                        final.append(ra[i])
                        final.append(la[i])
                    final.append(ra[-1])
                    print(*final)
                
        else:
            for i in range(len(ra)):
                final.append(la[i])
                final.append(ra[i])
            final.append(la[-1])
            print(*final)
    



        
