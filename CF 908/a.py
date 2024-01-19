from collections import defaultdict,Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    g=defaultdict(int)
    for ele in s:g[ele]+=1
    if g['A']>g['B']:
        i=0
        f=False
        for l in range(2,len(s)+1):
            g=Counter(s[:l])          
            if g['B']>=g['A']:f=True;break
            for j in range(l,len(s)):
                g[s[j]]+=1
                g[s[j-l]]-=1
                if g['B']>=g['A']:f=True;break
        if f:
            print('?')
        else:
            print('A')

    elif g['B']>g['A']:
        i=0
        f=False
        for l in range(2,len(s)+1):
            g=Counter(s[:l])           
            if g['A']>=g['B']:f=True;break
            for j in range(l,len(s)):
                g[s[j]]+=1
                g[s[j-l]]-=1
                if g['A']>=g['B']:f=True;break
        if f:
            print('?')
        else:
            print('B')
    else:
        print('?')
    print('upar')