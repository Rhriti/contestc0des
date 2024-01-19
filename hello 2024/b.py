for _ in range(int(input())):
    n=int(input())
    s=input()
    sums=0
    for ele in s:
        if ele=='+':sums+=1
        else:sums-=1
    print(abs(sums))
