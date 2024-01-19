for _ in range(int(input())):
    n=int(input())
    if n<3:
        print(-1)
    else:
        if n%2==1:
            print(1,1,(n-1)//2)
        else:
            if n%3==0:
                print(n//3,n//3,n//3)
            else:
                print(-1)
