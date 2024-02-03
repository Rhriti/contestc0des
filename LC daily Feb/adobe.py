
s='20'
sets={0,1,6,8,9}
arr=[0,1,6,8,9]
import bisect 

def f(i):
    if i==len(s)-1:
        index=bisect.bisect_right(arr,int(s[i]))
        return index-1

    count=5*(len(s)-i-1)-1
    for ele in [1,6,8,9]:
        if ele<int(s[i]):
            count+=5**(len(s)-i-1)

    if int(s[i]) in [1,6,8,9]:
        count+=f(i+1)
    return count

print(f(0))