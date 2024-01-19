for _ in range(int(input())):
    a,b,c=map(int,input().split())
    arr=[a,b,c]
    arr.sort()
    if a==b==c:
        print('YES')
    elif a==b or b==c or c==a:
        # if max(a,b,c)==2*min(a,b,c) or max(a,b,c)==3*min(a,b,c) or max(a,b,c)==4*min(a,b,c):
        #     print('YES')
        # else:print('NO')
        if arr[1]==arr[2]:
            if arr[1]==2*arr[0]:
                print('YES')
            else:print('NO')
        else:
            if arr[2]==2*arr[0] or arr[2]==3*arr[0] or arr[2]==4*arr[0]:
                print('YES')
            else:print('NO')
    else:
        arr.sort()
        if arr[2]==3*arr[0] and arr[1]==2*arr[0]:
            print('YES')
        else:
            print('NO')