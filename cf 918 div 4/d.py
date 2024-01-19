for _ in range(int(input())):
    n=int(input())
    s=input()
    V={'a','e'}
    C={'b','c','d'}
    newarr=[]

    i=n-1
    while i>0:
        if s[i] in V:
            newarr.append([s[i-1],s[i]])
            i-=2
        else:
            newarr.append([s[i-2],s[i-1],s[i]])
            i-=3
    
    newarr=newarr[::-1]
    snew=''
    for j in range(len(newarr)-1):
        for ele in newarr[j]:
            print(ele,end='')
        print('.',end='')
    for ele in newarr[-1]:
        print(ele,end='')
    print()
    
