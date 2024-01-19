#User function Template for python3

def minJumps(arr, n):
    #code here
    ans=[False for _ in range(len(arr))]
    def jumps(index):
        if arr[index]==0:
            if index==len(arr)-1:
                ans[index]=True
                return True
            else:
                ans[index]=False
                return False
        if arr[index]>=len(arr)-1-index:
            ans[index]=True
            return True
        else:
            t=False
            for i in range(index+1,index+arr[index]+1):
                t=t or jumps(i)
            ans[index]=t
            return t
    jumps(0)
    #base
    if ans[0] is False:
        return -1
    s=[]
    go=[]
    for i in range(len(arr)):
        if ans[i] is True:
            go.append(i)
            s.append(i)
        else:
            go.append(s[-1])
    print(go)    
    print(ans)
    j=0      
    i=0
    prev=0
    while i<len(arr)-1:
        if ans[i]:
            j+=1
            prev=i
            i=i+arr[i]
            
        else:
            if go[i]==prev:
                return -1
            else:
                i=go[i]
            
    
    return j

print(minJumps([2 ,3 ,1 ,1 ,2 ,4 ,2 ,0 ,1 ,1],10))
            
    #kaafi lamba ja rha h but no worries
    
            
        
