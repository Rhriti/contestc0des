class Solution:
    def findMaximumLength(self, nums ) :
        if len(nums)==1:return 1
     
        i=1
        final=[nums[0]]
        prev=final[-1]
        
        
        while i<len(nums):
            if nums[i]< final[-1]:
                sums=0
                j=i
                while j<len(nums) and sums<final[-1]:
                    sums+=nums[j]
                    j+=1
                    
                if sums>=final[-1]:
                    final.append(sums)
                    eat=j-i
                else:
                    eat=float('inf')

                

                sums2=0
                j=i
                while j>=0 and sums2<final[-1]:
                    sums2+=nums[j]
                    j-=1
                    
                if sums2>=final[-1]:
                    eatnew=i-j
                else:
                    eatnew=float('inf')
                

                if eatnew<eat:
                    floa

                

                #     t=sums
                #     flag=False
                    
                #     for k in range(len(final)-1,-1,-1):
                #         out=final.pop()
                #         t+=out
                #         if final and t>final[-1]:
                #             flag=True
                #             final.append(t)
                #             break
                             
                #     if not flag:
                #         return 1
                # i=j
                        
            else:
                final.append(nums[i])
                i+=1
                
        return len(final)
                
            
s=Solution()
print(s.findMaximumLength([272,482,115,925,983]))