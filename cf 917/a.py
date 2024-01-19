for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    no=0
    zero=False

    for ele in arr:
        if ele<0:no+=1
        if ele==0:
            zero=True


    if no%2==1:
        print(0)
    else:
        if zero:print(0)
        else:
            print(1)
            print(1,0)
    

    