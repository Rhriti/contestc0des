from collections import Counter,defaultdict

def minWindow( s , t ) :
    want=Counter(t)
    curr=defaultdict(int)
    i=j=0
    minm=float('inf')
    count=0
    
    for i in range(len(s)):
        
        while count<len(want) and j<len(s):
            if s[j] in want :
                curr[s[j]]+=1
                #base
                if curr[s[j]]==want[s[j]]:
                    count+=1
                    print(count)
                j+=1
                
        if count==len(want):
            if j-i-1<minm:
                minm=j-i+1
                ans=s[i:j+1]
        if s[i] in want:
            curr[s[i]]-=1
            if curr[s[i]]<want[s[i]]:
                count-=1
        
    return ans
print(minWindow('ADOBECODEBANC','ABC'))
        
        