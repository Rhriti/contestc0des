for _ in range(int(input())):
    n,k,x=map(int,input().split())
    if x>1:
        print('YES')
        print(n)
        for _ in range(n):
            print(1,end=' ')
        print()
    else:
        if k==1:
            print('NO')
        else:
            if k==2:
                if n%2==0:
                    print('YES')
                    print(n//2)
                    for _ in range(n//2):
                        print(2,end=' ')
                    print()
                else:
                    print('NO')
            else:
                print('YES')
                if n%2==0:
                    print(n//2)
                    for _ in range(n//2):
                        print(2,end=' ')
                    print()
                else:
                    if n==k:
                        print(1)
                        print(k)
                    else:
                        print(n//2)
                        for _ in range((n//2)-1):
                        
                            print(2,end=' ')
                        print(3)


                    
            