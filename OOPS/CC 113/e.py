
# def maxSubArray(nums):
#     cur_max, max_till_now = 0, -float('inf')
#     for c in nums:
#         cur_max = max(c, cur_max + c)
#         max_till_now = max(max_till_now, cur_max)
#     return max_till_now


# for _ in range(int(input())):
#     x,y=map(int,input().split())
#     if y>x:
#         big=y
#         bigval=-2
#         small=x
#         smallval=1
#     else:
#         big=x
#         bigval=1
#         small=y 
#         smallval=-2
#     if x==y:
#         arr=[1,-2]*x
#         print(maxSubArray(arr))
#     else:
    
#         fac=big//(small+1)
#         rem=x+y-(small*(fac+1))
#         arr=[bigval for _ in range(fac)]
#         arr.append(smallval)
#         arr=arr*small
#         for _ in range(rem):arr.append(bigval)
#         # arr=[bigval for _ in range(x+y)]
#         # #new


#         # c=0
#         # for i in range(fac,x+y,fac):
#         #     arr[i]=smallval
#         #     c+=1
#         #     if c>small:
#         #         arr[i]=bigval
#                 # break
     
#         print(maxSubArray(arr))





