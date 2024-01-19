from collections import Counter
import math
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s , k ) :
        g=Counter(s)
        arr=[]
        for vals in g.values():arr.append(vals)
        gnew=Counter(arr)
        arr.sort(reverse=True)
        if len(g)<k:
            return 0
        index=arr[k-1]
        ways=1
        for i in range(k):
            if arr[i]==index:
                left=k-(i)
                ways=ways*(  math.factorial(gnew[index])/ (math.factorial(gnew[index]-left) *math.factorial(left) ) )*index
                break
            else:
                ways=ways*arr[i]
        print(ways)
        return int(ways)
            
        
        
x=Solution()
x.countKSubsequencesWithMaxBeauty('lelxul',1)
        