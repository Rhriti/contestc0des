for _ in range(int(input())):
    n,d,h=map(int,input().split())
    y=list(map(int,input().split()))
    area=0.0
    st=[]
    for i in range(len(y)):
        if not st:
            st.append(y[i])
            continue

        if abs(y[i]-st[-1])<h:
            dh=abs(h-abs(y[i]-st[-1]))
            dx=d*dh/h
            area+=((d*h)/2)-((dh*dx)/2)
            # print(f'area of half ia {area}')
            st.pop()
            st.append(y[i])
        else:
            area+=(d*h)/2
            st.pop()
            st.append(y[i])
            # print(f'1st {area}')
    
    if st:
        area+=(d*h)/2
    print(area)
