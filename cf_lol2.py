for _ in range(int(input())):
    final=[]
    for _ in range(8):
        s=input()
        t=[ele for ele in s]
        final.append(t)

    st=[]
    for c in range(8):
        for r in range(8):
            if final[r][c]!='.':
                st.append(final[r][c])
        if len(st)>0:
            break
    for ele in st:
        print(ele,end='')
    print()
