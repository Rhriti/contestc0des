#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        Parr=Parr.sort(key= lambda x:x.a)
        prev=Parr[0].b
        c=0
        maxm=0
        for i in range(1,len(Parr)):
            if Parr[i].b>prev:
                prev=Parr[i].b
                c+=1
                maxm=max(maxm,c)
            else:
                c=0
        return max(maxm,c+1)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))
        obj=Solution()
        print(obj.maxChainLen(Parr, n))
# } Driver Code Ends