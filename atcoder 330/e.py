# import heapq as hq
# from collections import Counter
# n,q=map(int,input().split())
# arr=list(map(int,input().split()))

# g=Counter(arr)
# st=[]
# for ele in range(10**5+10):
#     if ele not in g:hq.heappush(st,ele)
# #
# newadd=set()
# for _ in range(q):
#     i,x=map(int,input().split())
#     bahar=arr[i-1]
#     arr[i-1]=x
#     g[bahar]-=1
#     newadd.add(x)

#     if g[bahar]<=0:
#         hq.heappush(st,bahar)
#         if bahar in newadd:newadd.remove(bahar)

#     while st and st[0] in newadd:
#         out=hq.heappop(st)

#     mex=hq.heappop(st)
#     print(mex)


import heapq

n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Create a set for fast lookup of elements in the array
elements = set(arr)

# Create a heap with all potential MEX values
heap = [i for i in range(10**5+1) if i not in elements]
heapq.heapify(heap)

for _ in range(q):
    i, x = map(int, input().split())
    i -= 1  # Convert to 0-based index

    # If the old value is not in the array anymore, remove it from the heap
    if arr[i] not in elements:
        heap.remove(arr[i])
        heapq.heapify(heap)

    # Add the new value to the array and the set
    arr[i] = x
    elements.add(x)

    # Remove all elements from the heap that are in the array
    while heap and heap[0] in elements:
        heapq.heappop(heap)

    # The MEX is the smallest element in the heap
    print('mex',heap[0])