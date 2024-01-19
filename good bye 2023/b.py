import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    o={};e={}
    for ele in arr:
        if ele%2==0:e.add(ele)
        else:o.add(ele)
    
    #even=mayla
    #odd=oyla
    i=0
    while len(e)+len(o)!=1:
        if i%2==0:
            if len(e)>=2:
                e1,e2=e.pop(),e.pop()
                e.add((e1+e2)//2)
            elif len(e)==1:
                f=2*(math.floor((e.pop()+o.pop())/2))
                e.add(f)
            else:
                f=2*(math.floor((o.pop()+o.pop())/2))
                e.add(f)
        else:
            if len(e)>1 and len(o)>1:
                e1,o1=e.pop(),o.pop()
                e.add(2*math.floor((e1+o1)/2))
            else:
                if len(e)>=2:
                    e.add((e.pop()+e.pop())//2)
                else:
                    e.add( 2*math.floor((o.pop()+o.pop())/2)    )
        i+=1

    if  i%2==0:
        print()
    