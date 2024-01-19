import itertools

def minimumString( a , b , c ):
    
    def add(n1,n2):
        count=0
        for i in range(len(n2)+1):
            news=n2[:i]
            if n1.endswith(news):
                count=max(count,i)
        return count

        
    final=[]
    perm=list(itertools.permutations([a,b,c]))
    for a1,b1,c1 in perm:
        if b1 not in a1:
            cnew=add(a1,b1)
            cnew=a1+b1[cnew:]
            if c1 not in cnew:
                c2=add(cnew,c1)
                cnew=cnew+c1[c2:]
            final.append(cnew)
        else:
            cnew=a1
            if c1 not in cnew:
                c2=add(cnew,c1)
                cnew=cnew+c1[c2:]
            final.append(cnew)
            
    final.sort(key=len)
    print(final)
    ans=final[0]
    l=len(ans)
    for i in range(1,len(final)):
        if len(final[i])==l:
            ans=min(ans,final[i])
    print(ans)

                

minimumString("abc",
"bca",
"aaa")