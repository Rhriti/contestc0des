class Solution:
    def longestPalindrome(self, words ) :
        from collections import Counter
        g=Counter(words)
        n=0
        f=0
        
        for word in g.keys():
            if word[0]==word[1]:
                n+=2*(g[word]-(g[word]%2))
                g[word]=g[word]%2
                if g[word]==1:
                    f=1
                    
            else:
                if word[::-1] in g:
                    n+=4* min(g[word],g[word[::-1]])
                    g[word]=0
                    g[word[::-1]]=0
                else:
                    g[word]=0
            
        if f==1:
            n+=2
        return n