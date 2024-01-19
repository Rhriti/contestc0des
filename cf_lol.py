for _ in range(int(input())):
    n=int(input())
    st=[]
    for i in range(1,n+1):
        a,b=map(int,input().split())
        st.append([b,a,i])
    st.sort(reverse=True)
    for ele in st:
        if ele[1]<=10:
            print(ele[2])
            break