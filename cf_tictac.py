from collections import defaultdict
for _ in range(int(input())):
    r={0:set(),1:set(),2:set()}
    c={0:set(),1:set(),2:set()}
    g=[]
    for i in range(3):
        s=input()
        a=s[0]
        b=s[1]
        c_=s[2]
        g.append([a,b,c_])
        r[i].add(a)
        r[i].add(b)
        r[i].add(c_)
        c[0].add(a)
        c[1].add(b)
        c[2].add(c_)
    f=False
    for val in r.values():
        if len(val)==1:
            out=val.pop()
            if out!='.':   
                f=True 
                print(out)
            else:
                val.add(out)
            
    for val in c.values():
        if len(val)==1:
            out=val.pop()
            if out!='.':
                f=True
                print(out)
            else:
                val.add(out)

    if g[0][0]==g[1][1]==g[2][2] and g[0][0]!='.':
        f=True
        if g[0][0]=='X':
            print('X')
        if g[0][0]=='O':
            print('O')
        if g[0][0]=='+':
            print('+')
    if g[0][2]==g[1][1]==g[2][0] and g[1][1]!='.':
        f=True
        if g[1][1]=='X':
            print('X')
        if g[1][1]=='O':
            print('O')
        if g[1][1]=='+':
            print('+')    
    if not f:
        print('DRAW')
    
