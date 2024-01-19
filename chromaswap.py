for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    col_A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    col_B=list(map(int,input().split()))
    bset=set(col_B)
    index=set()
    for i in range(n):
        if col_A[i] not in bset:index.add(i)

    arr=[]
    for i in range(n):
        arr.append([A[i],col_A[i]])
        arr.append([B[i],col_B[i]])
    arr.sort()
    newarr=[-1]

    for j in range(len(arr)):
        if len(newarr)-1 in index:
            if A[len(newarr)-1]>=newarr[-1]:
                newarr.append(A[len(newarr)-1])
            else:break 
        else:
            if arr[j][1]==col_A[len(newarr)-1]:
                if arr[j][0]>=newarr[-1]:newarr.append(arr[j][0])
        if len(newarr)==n+1:break
    print('YES') if len(newarr)==n+1 else print('NO')

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     cola = list((map(int, input().split())))
#     b = list(map(int, input().split()))
#     colb = list((map(int, input().split())))
    
#     values = [ [] for _ in range(2*n+1)]
#     canswap = set(colb)
#     for i in range(n):
#         values[cola[i]].append(a[i])
#         values[colb[i]].append(b[i])
#     for i in range(2*n+1): values[i] = sorted(values[i])[::-1]
    
#     ans = []
#     for i in range(n):
#         if cola[i] not in canswap:
#             ans.append(a[i])
#             continue
#         while values[cola[i]]:
#             if len(ans) and values[cola[i]][-1] < ans[-1]:
#                 values[cola[i]].pop()
#             else: break
#         if values[cola[i]]:
#             ans.append(values[cola[i]][-1])
#             values[cola[i]].pop()
#     if len(ans) == n and ans == sorted(ans):
#         print('Yes')
#     else:
#         print('No')


   
