for _ in range(int(input())):
    n=input()
    x=int(input())
    n1=input()
    n2=input()
    d=[]
    for i in range(x):
        t=set()
        for j in range(min(int(n1[i]),int(n2[i])),max(int(n1[i]),int(n2[i]))+1):
            t.add(str(j))
        d.append(t)
    
    index=0
    ans='YES' #password possible
    for ele in n:
        if ele in d[index]:
            d[index].remove(ele)
        if len(d[index])==0:
            index+=1
        if index==len(d):
            ans='NO'
            break
    print(ans)

    
    
            
    
        