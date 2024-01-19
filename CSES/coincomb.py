n,x=map(int,input().split())
import sys
sys.setrecursionlimit(10**6)
arr=list(map(int,input().split()))
memo={}
def dp(rem):
    if rem in memo:
        return memo[rem]
    if rem==0:
        return 1
    if rem<0:
        return 0
    ways=0
    for ele in arr:
        ways+=dp(rem-ele)
    memo[rem]=ways
    return ways
    
print(dp(x))