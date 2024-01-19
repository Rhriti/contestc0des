
for _ in range(int(input())):
    s1,s2=input().split()
    if len(s1)<len(s2):
        d=len(s2)-len(s1)
        s1='0'*d+s1
    if len(s2)<len(s1):
        d=len(s1)-len(s2)
        s2='0'*d+s2
    
    c=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            c+=abs(int(s1[i])-int(s2[i]))+9*(len(s1)-i-1)
            break
    print(c)

                  
