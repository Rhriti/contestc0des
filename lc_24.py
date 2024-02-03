
def maxLength(arr ):
    
    def func(i,s):
        if i==len(arr):
            final[0]=max(final[0],len(s));return 
        
        f=False
        snew=set()
        for ele in arr[i]:
            snew.add(ele)
            if ele in s:f=True;break
        if snew!=len(arr[i]):
            func(i+1,s)
        else:
            if f:
                func(i+1,s)
            else:
                for ele in arr[i]:s.add(ele)
                func(i+1,s)
                for ele in arr[i]:s.remove(ele)
                func(i+1,s)
            
    final=[0]
    func(0,set())
    return final[0]
            
        
print(maxLength(['aa','bb']))