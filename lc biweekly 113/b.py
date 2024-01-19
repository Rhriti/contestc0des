from collections import Counter

def minLengthAfterRemovals( nums ):
    g=Counter(nums)
    same=[]
    newarr=[]
    for ele in nums:
        if g[ele]>1:
            same.append(ele)
        else:
            newarr.append(ele)
    st=[]
    for ele in same:
        if len(st)==0:st.append(ele)
        else:
            if ele>st[-1]:
                st.pop()
            else:
                st.append(ele)
    print(newarr)
    if len(st)==0:
        if len(newarr)%2==0:
            return 0
        else:return 1
        
    else:
        newarr.extend(st)
        newarr.sort()
        st=[]
        for ele in newarr:
            if len(st)==0:st.append(ele)
            else:
                if ele>st[-1]:
                    st.pop()
                else:
                    st.append(ele)
        return len(st)
        
print(minLengthAfterRemovals([1]))