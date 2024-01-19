class Solution:
    def largestVariance(self, s ) :
        v=set()
        lst=[]
        for ele in s:
            if ele not in v:
                v.add(ele)
                lst.append(ele)
        maxm=0
        for i in range(len(lst)-1):
            for j in range(i+1,len(lst)):
                maxm=max(maxm,self.maxv(lst[i],lst[j],s))
        return maxm
    
    def maxv(self,a,b,s):
        bc=0
        ac=0
        maxm_b=0
        for i in range(len(s)):
            if s[i]==a or s[i]==b:
                if ac==0 and bc==0:
                    if s[i]==b:
                        bc+=1
                else:
                    if s[i]==b:
                        bc+=1
                        maxm_b=max(maxm_b,bc-ac)
                    else:
                        ac+=1
                        if ac>=bc:
                            ac=0
                            bc=0
        
        maxm_b=max(maxm_b,bc-ac)
        # print(f'b is {b} maxm_b is {maxm_b}')
        
        bc=0
        ac=0
        maxm_a=0
        for i in range(len(s)):
            if s[i]==a or s[i]==b:
                if ac==0 and bc==0:
                    if s[i]==a:
                        ac+=1
             
                else:
                    if s[i]==a:
                        ac+=1
                        maxm_a=max(maxm_a,ac-bc)
                    else:
                        bc+=1
                        if bc>=ac:
                            ac=0
                            bc=0
        
        maxm_a=max(maxm_a,ac-bc)
        # print(f'a is {a} maxm_b is {maxm_a}')
        return max(maxm_a,maxm_b)
                
        
        
        


    
