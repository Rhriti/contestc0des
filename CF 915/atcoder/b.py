n=int(input())
input()
def dp(node):
    if node==1:return 1
    if node==2:return 2
    if node==3:return 4

    t=0
    for ch in range(1,node+1):
        t+=dp(ch)
    return t

print('ans',dp(n)%(10**9+7))
        


