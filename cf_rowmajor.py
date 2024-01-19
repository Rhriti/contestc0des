for _ in range(int(input())):
    n=int(input())
    if n==1:
        print('a')
    else:
        notdiv=None
        for i in range(1,n+1):
            if n%i!=0:
                notdiv=i
                break
        if notdiv is None:
            s=[]
            for ele in range(ord('a'),ord('a')+n,1):
                s.append(chr(ele))
            for ele in s:
                print(ele,end='')
            print()
        else:
            s=[]
            t=n//notdiv
            for ele in range(ord('a'),ord('a')+notdiv,1):
                s.append(chr(ele))
            s=s*t
            for ele in range(ord('a'),ord('a')+(n%notdiv),1):
                s.append(chr(ele))
            for ele in s:
                print(ele,end='')
            print()
