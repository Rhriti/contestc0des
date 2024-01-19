for _ in range(int(input())):
    n=int(input())
    s=str(n)
    if s[0]=='1':
        sums=0
        for i in range(1,len(s)):
            if s[i]!='0':
                sums+=min(abs(int(s[i])-int(s[i-1])),10- abs(int(s[i])-int(s[i-1])) )
            else:
                sums+=min(10-int(s[i]),int(s[i]))
        sums+=len(s)
        print(sums)
    else:
        sums=0
        for i in range(1,len(s)):
            if s[i]!='0':
                sums+=min(abs(int(s[i])-int(s[i-1])),10- abs(int(s[i])-int(s[i-1])) )
            else:
                sums+=min(10-int(s[i]),int(s[i]))
        sums+=len(s)
        if s[0]!='0':
            sums+=min(abs(int(s[0])-1),10-abs(int(s[0])-1))
        else:
            sums+=1
        print(sums)
    print('ans')

