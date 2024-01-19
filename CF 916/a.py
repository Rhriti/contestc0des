from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    g=Counter(s)
    c=0
    for k,v in g.items():
        if v>= ord(k)-ord('A')+1:c+=1
    print(c)