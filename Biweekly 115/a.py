
def lastVisitedIntegers(words=["1","prev","2","prev","prev"]) :
    st=[]
    final=[]
    i=0
    while i<len(words):
        if words[i]=='prev':
            c=0
            f=False
            for j in range(i,len(words)):
                if words[j]!='prev':
                    break
                else:
                    if j==len(words)-1:
                        f=True
                    c+=1
            i=j #next yahi se chalu hoga
            for k in range(min(c,len(st))):
                final.append(st[len(st)-1-k])
            left=c-len(st)
            if left>0:
                for _ in range(left):
                    final.append(-1)
            if f:
                return final
            
        else:
            st.append(int(words[i]))
            i+=1
    return final
            
print(lastVisitedIntegers())  
    