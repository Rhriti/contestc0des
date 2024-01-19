for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    if s[-1]==1:
        print('NO')
    else:
        st=[]
        order=[]
        for i in range(len(s)):
            if s[i]==1:
                st.append(1)
            else:
                order.append(len(st))
                for _ in range(len(st)):
                    order.append(0)
                st=[]
        print('YES')
        order.reverse()
        for ele in order:
            print(ele,end=' ')
        print()