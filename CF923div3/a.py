for _ in range(int(input())):
    n=int(input())
    s=input()
    f=False
    for i in range(len(s)):
        if s[i]=='B':
            f=True
            break 
    if not f:
        print(0)
    else:
        for j in range(len(s)-1,-1,-1):
            if s[j]=='B':break 
        print(j-i+1)
    
