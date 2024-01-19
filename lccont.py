
def canSplitArray( nums ,m ) :
    if len(nums)==1:
        return True
    pres=[]
    s=0
    for ele in nums:
        s+=ele
        pres.append(s)      
    
    def f(i,j):
        #base
        if j-i==1:
            return True
        
        t=False
        sums=0
        for index in range(i,j):
            sums+=nums[index]
            if index ==i:
                if pres[j]-pres[i]>=m and f(i+1,j):
                    t=True
            elif index==j-1:
                if i==0:
                    if pres[j-1]>=m and f(i,j-1):
                        t=True
                else:
                    if pres[index]-pres[i-1]>=m and f(i,j-1):
                        t=True
            else:
                if sums>=m and pres[j]-pres[index]>=m and f(i,index) and f(index+1,j):
                    t=True
        return t
    return f(0,len(nums)-1)
                
        
print(canSplitArray([1,2,1,1],4))