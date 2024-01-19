import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==2:
        print(arr[0])
        continue
    final=[]
    news=set()
    for d in range(0,10):
        newarr=[]
        for ele in arr:newarr.append(ele+d)
        for i in range(n):
            for j in range(i+1,n):
                news.add(math.gcd(arr[i],arr[j]))
    
    f=False
    for ele in news:
        s=set()
        for nums in arr:s.add(nums%ele)
        if len(s)==2:
            f=True
            print(ele)
            break
    if not f:
        print(1000000000000000000)






    # news=list(news)
    # news.sort()
    # print('ans',news[1])
    
    # f=False
    # for ele in final:
    #     s=set()
    #     for nums in arr:s.add(nums%ele)
    #     if len(s)==2:
    #         f=True
    #         print(ele)
    #         break
 
    # print('upar')


    # f=False
    # for ele in news:
    #     s=set()
    #     for num in arr:
    #         s.add(num%ele)
    #     if len(s)==2:
    #         f=True
    #         print(ele)
    #         break
    # if not f:
    #     print('1'+'0'*18)
   
    
# import math
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     arr.sort()
#     diffs = [arr[i+1] - arr[i] for i in range(n-1)]
#     f=False
#     for diff in diffs:
#         s=set()
#         for num in arr:
#             s.add(num%diff)
#         if len(s)==2:
#             f=True
#             print(diff)
#             break
#     if not f:
#         print('1'+'0'*18)


# import math
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     f=False
#     for d in range(0,10):
#         newarr=[]
#         for ele in arr:newarr.append(ele-d)
#         s=set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 s.add(math.gcd(newarr[i],newarr[j]))
        
#         print(s,'d',d)
#         if len(s)==1 and d!=1:
#             f=True
#             print(d)
#             break
        
#     if not f:
#         print(1000000000000000000)
    
#     print('upar')