s=input()
st=[]
for ele in s:
    st.append(ele)
    if len(st)>=3:
        if st[-1]=='C' and st[-2]=='B' and st[-3]=='A':
            st.pop()
            st.pop()
            st.pop()
final=''
for ele in st:final+=ele
print(final)

