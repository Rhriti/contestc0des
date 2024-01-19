for _ in range(int(input())):
    g=[]
    ans=None
    for _ in range(3):
        s=input()
        sets={'A','B','C'}
        if '?' in s:
            for ele in s:
                if ele in sets:sets.remove(ele)
            ans=sets.pop()
    print(ans)
