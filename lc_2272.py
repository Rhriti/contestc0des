from collections import defaultdict
class Solution:
    def largestVariance(sef, s) :
        g=defaultdict(int)
        i=j=0
        maxm=0
        while j<len(s):

            val_set=set()
            while len(g)<=2 and j<len(s):
                g[s[j]]+=1
                val_set.add(s[j])
                j+=1
            del g[s[j-1]]
            val_set.remove(s[j-1])
            if len(val_set)==2:
                maxm=max(maxm,abs(g[val_set.pop()]-g[val_set.pop()]))
            while len(g)==2 and i<=j:
                if s[i] in g and g[s[i]]>=1:
                    g[s[i]]-=1
                    if g[s[i]]==0:
                        del g[s[i]]
                maxm=max(maxm,max(g.values())-min(g.values()))
                i+=1

            if j-1<len(s):
                g[s[j-1]]+=1
        return maxm

s=Solution()
print(s.largestVariance("icexiahccknibwuwgi"))