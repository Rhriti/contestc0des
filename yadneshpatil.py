def solve(S1,S2):
   
    c2=0
    for i in range(len(S1)-1,-1,-1):
        if S1[i]==S1[0]:
            c2+=1
        else:break
    tarr=[]
    for i in range(len(S2)):
        if S2[i]=='T':
            tarr.append(i)
    t=True
    for i in range(1,len(tarr)):
        if tarr[i]<tarr[i-1]+(len(S1)-c2):
            t=False
            break
    if t:
        final='A'*tarr[0]
        for i in range(len(tarr)-1):
            final+=S1[:min(tarr[i+1]-tarr[i],len(S1))]
            if tarr[i+1]-tarr[i]>len(S1):
                final+='A'*(tarr[i+1]-tarr[i]-len(S1))
        final+=S1
        lefts=len(S2)-tarr[-1]-1
        final+='A'*lefts
        print(final)
        if len(final)==len(S1)+len(S2)-1:
            return final
        else:
            return -1
        #last add krde
    else:
        return -1

    
print(solve('ABC','FFFFTFT'))