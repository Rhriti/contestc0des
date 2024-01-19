
def canMakeSubsequence( str1 , str2 ) :
    i=0
    j=0
    next={}
    for ele in range(ord('a'),ord('a')+26):
        next[chr(ele)]=chr(ele+1)
    next['z']='a'

    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j] or next[str1[i]]==str2[j]:
            i+=1
            j+=1
        else:
            i+=1
            
    if j==len(str2):
        return True
    else:
        return False

print(canMakeSubsequence('zc','ad'))
