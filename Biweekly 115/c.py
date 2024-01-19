import copy 
def getWordsInLongestSubsequence( n , words, gro) :
    def hd(i,j):
        c=0
        for k in range(len(words[i])):
            if words[i][k]!=words[j][k]:
                c+=1
        if c==1:return True
        return False
    
    def f(i):  
        if arr[i] is not None:return arr[i]
        
        maxm=[i]
        for j in range(i+1,len(words)):
            if len(words[j])==len(words[i]) and hd(i,j) and gro[i]!=gro[j]:
                nxt=f(j)
                nxt.append(i)
                maxm=max(maxm,nxt,key=len)
        arr[i]=copy.deepcopy(maxm)
        return maxm
    
    final=[]
    for index in range(len(words)):
        arr=[None for _ in range(n)]
        final=max(final,f(index),key=len)
    ans=[]
    for ele in final:
        ans.append(words[ele])
    return ans[::-1]
    

print(getWordsInLongestSubsequence(
    4,
["a","b","c","d"],
[1,2,3,4]
))