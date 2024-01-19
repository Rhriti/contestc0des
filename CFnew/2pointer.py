from collections import defaultdict
def longestKSubstr( s, k):
        curr=defaultdict(int)
        maxm=-1
        i=j=0
        for i in range(len(s)):
            while j<len(s) and ((len(curr)<k and s[j] not in curr)  or (s[j] in curr and len(curr)<=k)):
                curr[s[j]]+=1
                j+=1
            if len(curr)==k:
                maxm=max(maxm,j-i)
            # print(s[i:j])
            curr[s[i]]-=1
            if curr[s[i]]==0:
                del curr[s[i]]
        return maxm

#time complexity of above code is O(n) and space complexity is O(k)
#it is giving TLE on gfg because of the use of defaultdict, why is it so?
