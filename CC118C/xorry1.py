for _ in range(int(input())):
    x=int(input())
    binx=bin(x)[2:]
    a=['0']*len(binx)
    b=['0']*len(binx)
    c=0
    
    for i in range(len(binx)):
        if binx[i]=='1':
            if c%2==0:a[i]='1'
            else:b[i]='1'
            c+=1
    s1=''.join(a)
    s2=''.join(b)
    print(s1,s2)
    print(min(int(s1,2),int(s2,2)),max(int(s1,2),int(s2,2)))
    

    
    