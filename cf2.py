for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    #2 jis taraf hai us taraf maaxdaldo
    index1=d.index(1)
    index2=d.index(2)
    if abs(index1-index2)>=2:
        if index2>index1:
            print(f'{index1+2} {d.index(max(d))+1}')
        else:
            print(f'{index1} {d.index(max(d))+1}')
    else:
        if index1-index2==1:  #....21..
            if len(d)-1-index1>index2:
                print(f'{index1+1} {len(d)}')
            else:
                print(f'{1} {index2+1}')
        else:     #...12....
            if len(d)-1-index2>index1:
                print(f'{index2+1} {len(d)}')
            else:
                print(f'{1} {index1+1}')


