# cook your dish here
import math
import bisect
def findNumber(a, n, K):

	low = 0
	high = n - 1

	# Binary search
	while (low <= high):

		# Find the mid element
		mid = (low + high) >> 1

		# If element is found
		if (K >= a[mid][0] and K <= a[mid][1]):
			return mid

		# Check in first half
		elif (K < a[mid][0]):
			high = mid - 1

		# Check in second half
		else:
			low = mid + 1

	# Not found
	return -1

for _ in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    que=[]
    for _ in range(q):
        que.append(int(input()))
    ranges=[]
    prev=0
    ans=[]
    for i in range(len(arr)-2):
        ans.append(arr[i])
        add=((len(arr)-1 -i)*(len(arr)-2-i))//2 
        ranges.append([prev,prev+add-1])
        prev=ranges[-1][1]+1



    # Driver code
    a= ranges
    n = len(a)
    final=[]
    for ele in que:
        k = ele-1
        index = findNumber(a, n, k)
        print(ans[index])



# This code is contributed by mohit kumar


    
    
    
    
    
    
    
        