for _ in range(int(input())):
    n=int(input())
    if n==1:
        print('1')
    elif n==2:
        print('2 1')
    else:
        ans=[2]
        mid=n//2
        k=4
        for i in range(n):
            if i==0 or i==n-1:
                continue
            if i==mid:
                ans.append(1)
            else:
                ans.append(k)
                k+=1

        ans.append(3)
        for ele in ans:
            print(ele,end=' ')
        print()





        

