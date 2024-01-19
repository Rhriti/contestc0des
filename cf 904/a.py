for _ in range(int(input())):
    x,k=map(int,input().split())
    while True:
        s=str(x)
        sums=0
        for ele in s:sums+=int(ele)
        if sums%k==0:
            print(x)
            break
        x+=1
    print('upar')
