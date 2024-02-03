for _ in range(int(input())):
    n,k,m=map(int,input().split())
    s=input()
    need=n-1
    sets={chr(ele) for ele in range(ord('a'),ord('a')+k)}
    inmese={chr(ele) for ele in range(ord('a'),ord('a')+k)}
    f=True

    for i in range(m):

        if s[i] in sets:
            newset=set()
            c=0
            for j in range(i+1,m):
                if s[j] in inmese:newset.add(s[j])
                if len(newset)==k:
                    newset=set()
                    c+=1

            if c==need:sets.remove(s[i])
            else:
                f=False
                nahi_hai=inmese-newset
                final=s[i]+'a'*(need-len(nahi_hai))
                while nahi_hai:final+=nahi_hai.pop()
                break               
    
        if len(sets)==0:break
    


    if len(sets)==0:print('YES')
    else:
        if f is False:print('NO');print(final)
        else:print('NO');print(sets.pop()*n)
