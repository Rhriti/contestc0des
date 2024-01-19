from collections import Counter
for _ in range(int(input())):
    s=input()
    if s=='()':
        print('NO')
    else:
        st=[]
        f=False
        count=0
        for ele in s:
            if len(st)==0:
                st.append(ele)
                count+=1
            else:
                if ele=='(':
                    st.append(ele)
                    count+=1
                else:
                    if st[-1]=='(':
                        st.pop()
                        count-=1
                    else:
                        st.append(ele)
                        count+=1
            if count>=2:
                f=True
        print('YES')
        if len(st)!=0:
            g=Counter(st)
            if len(g)==1:
                ans='()'*len(s)
            else:
                if s[0]=='(':
                    ans='()'*len(s)
                else:
                    ans='('*len(s)+')'*len(s)
            print(ans)
        else:
            if f:
                ans='()'*len(s)
                print(ans)
            else:
                ans='('*len(s)+')'*len(s)
                print(ans) 