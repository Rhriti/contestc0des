for _ in range(int(input())):
    n=int(input())
    s=input()
    count=0
    sets=set()

    for i in range(n):
        if s[i] not in sets:
            sets.add(s[i])
            count+=n-i 
    print(count)
        


