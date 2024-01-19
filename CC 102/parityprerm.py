import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ne=no=0
    mod=10**9+7
    for ele in arr:
        if ele%2==1:no+=1
        else:ne+=1
    
    if n%2==0:
        if ne==no:
            print(2*math.factorial(no)*math.factorial(ne)%mod)
        else:print(0)
    else:
        if abs(no-ne)==1:
            print(math.factorial(no)*math.factorial(ne)%mod)
        else:
            print(0)