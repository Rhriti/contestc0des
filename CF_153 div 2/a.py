for _ in range(int(input())):
    s=input()
    ans1='()'*len(s)
    ans2='('*len(s)+')'*len(s)
    if s not in ans1:
        print('YES')
        print(ans1)
    elif s not in ans2:
        print('YES')
        print(ans2)
    else:
        print('NO')