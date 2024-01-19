import math
for _ in range(int(input())):
    n=int(input())
    index=None
    #i think odd even me divide karna is not effective and serves no purpose 
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            n=n//i
            index=i
            break
    if index is None:
        print('NO')
    else:
        s=[]
        F=False
        for j in range(i+1,int(math.sqrt(n))+1):
            if n%j==0:
                if i!=j!=(n//j):
                    F=True
                    print('YES')
                    print(i,j,n//j)
                    break
        if not F:
            print('NO')

        