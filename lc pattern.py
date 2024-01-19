class Solution:
    def find132pattern(self, nums ) :
        #soche ka antar tha , i was thinking form start but had to think form end
        arr=[None]*len(nums)
        st=[]
        for i in range(len(nums)-1,-1,-1):
            if len(st)==0:st.append(i)
            else:
                while st and nums[i]>nums[st[-1]]:
                    out=st.pop()
                    arr[out]=i
                st.append(i)
                
                
        minarr=[[nums[0],0]]
        for i in range(1,len(nums)):
            if nums[i]<minarr[-1][0]:
                minarr.append([nums[i],i])
            else:minarr.append([minarr[-1][0],minarr[-1][1]])
        #right se left chalte hai ab
        for i in range(len(nums)-1,-1,-1):
            if arr[i] is not None:
                if minarr[i][0]<nums[arr[i]]>nums[i] and nums[i]>minarr[i][0] and  minarr[i][1]<arr[i]<i:
                    return True
        return False
x=Solution()
x.find132pattern([3,5,0,3,4])