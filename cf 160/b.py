from collections import Counter
for _ in range(int(input())):
    s=input()
    g=Counter(s)
    
    count=0
    for i in range(len(s)):
        if s[i]=='1':
            if g['0']>=1:
                g['0']-=1
                count+=1
            else:
                break
        else:
            if g['1']>=1:
                g['1']-=1
                count+=1
            else:
                break
    
    print(len(s)-count)
        
        
