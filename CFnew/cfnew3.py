for _ in range(int(input())):
    n=list(map(int,input().split()))
    d=int(input())
    n1=list(map(int,input().split()))
    n2=list(map(int,input().split()))

    def f(index,sindex):
        print('wtfd')
        print(f'index {index} sindex {sindex}')
        if sindex==-1:
            return True
        else:
            if index==-1:
                return False
            
       
        if max(n1[sindex],n2[sindex])<=n[index]<=min(n1[sindex],n2[sindex]):
            ans=True
        else:
            ans=False
        if ans:
            for i in range(index):
                if f(i,sindex-1):
                    return True
            return False
        else:
            for i in range(index):
                if f(i,sindex):
                    return True
            return False
        

    for i in range(len(n)):

        if f(i,len(n1)-1):
            print('YES')
    print('NO')            