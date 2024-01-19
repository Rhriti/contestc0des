class Solution:
    def shortestBeautifulSubstring(self,s , k ) :
        index=[]
        for i in range(len(s)):
            if s[i]=='1':
                index.append(i)
        print(index)
        minm=float('inf')
        f=False

        for i in range(len(index)):
            j=i+(k-1)
            if j<len(index):
                f=True
                minm=min(minm,index[j]-index[i]+1)
        if not f:return ''
        final='1'*minm
        for i in range(len(index)):
            j=i+(k-1)
            if j<len(index) and index[j]-index[i]+1==minm:
                final=min(final,s[index[i]:index[j]+1])

        return final

# print(shortestBeautifulSubstring("1100100101011001001",
# 7))