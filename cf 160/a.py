for _ in range(int(input())):
    s=input()
    n=len(s)
    if n%2==1:
        t=False
        for i in range(1,n//2+1):
            if s[i]!='0':
                a=s[:i]
                b=s[i:]
                t=True
                break
        if t:
            print(a,b)
        else:print(-1)
    else:
        if n==2:
            if s[1]!='0' and int(s[1])>int(s[0]):print(s[0],s[1])
            else:print(-1)
        else:
            f=False
            for i in range(1,n//2):
                if s[i]!='0':
                    f=True
                    a=s[:i]
                    b=s[i:]
                    break
            
            if f:
                print(a,b)
            else:
                if s[n//2]!='0' and int(s[n//2:])>int(s[:n//2]):print(s[:n//2],s[n//2:])
                else:print(-1)
    