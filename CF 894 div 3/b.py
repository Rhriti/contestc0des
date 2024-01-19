for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    st=[b[0]]
    for i in range(1,len(b)):
        if b[i]>=st[-1]:
            st.append(b[i])
        else:
            st.append(1)
            st.append(b[i])
    print(len(st))
    for ele in st:
        print(ele,end=' ')
    print()