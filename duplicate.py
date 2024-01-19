class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        
        i=2
        while i<=len(nums)-1:
            if nums[i]==nums[i-2]:
                nums.pop(i)
                continue
            else:
                i+=1
        return len(nums)
        
        