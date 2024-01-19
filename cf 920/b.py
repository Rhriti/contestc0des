for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    sum1=0
    sum2=0
    com=0
    for i in range(n):
        if s1[i]==s2[i]=='1':com+=1
        if s1[i]=='1':sum1+=1
        if s2[i]=='1':sum2+=1
    sum1-=com
    sum2-=com
    print(max(sum1,sum2))
