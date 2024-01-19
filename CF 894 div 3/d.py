import math
for _ in range(int(input())):
    n=int(input())
    i=1
    j=1414213563
    while i<=j:
        mid=(i+j)//2
        ice_creams=((mid-1)*mid)//2
            
        if ice_creams>n:
            j=mid-1
        else:
            ans=mid
            i=mid+1
    # print('number of dsitinct balls ',ans)
    # ways=ans*(ans-1)/2
    ways2=ans*(ans-1)//2
    # print('ways ', ways)
    # print('ways2 ',ways2)
    # print('no. of balls 1 ',ans+(n-ways))
    # print('no of balls 2',ans+(n-ways2))
    print(ans+(n-ways2))
           

# def solve(now):
#     l = 1
# #    r = 2 * 10**9
#     r = 1414213563
#     ans = 0
    
#     while l <= r:
#         mid = (l + r) // 2

#         if mid * (mid - 1) // 2 <= now:
#             ans = mid
#             l = mid + 1
#         else:
#             r = mid - 1
    
#     ans_product = ans * (ans - 1) // 2
# #    print(f"ans: {ans}, ans_product: {ans_product}, l: {l}, r: {r}, now: {now}")
# #    print(f"ans + now: {ans + now}")

#     return ans + now - ans_product

# t = int(input())  

# for _ in range(t):
#     n = int(input())  
#     print(solve(n))





    