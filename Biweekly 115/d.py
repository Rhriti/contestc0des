class Solution:
    def countSubMultisets(self, nums, l , r ) :
        
        def f(i,l,r):
            #base
            if i==len(nums):return 0
            l-=nums[i]
            r-=nums[i]

            if l>0:
                return f(i+1,l,r)
            elif r>=0:
                return 1+ f(i+1,l,r)
            else:return 0
        return f(0,l,r)

            
        