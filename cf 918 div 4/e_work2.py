def function(a):
    n=len(a)
    hash={"0":0}
    count=0
    for i in range(n):
        if i%2==0:
            count+=a[i]
        else:
            count-=a[i]
        if str(count) in hash:
            return "YES"
        hash[str(count)]=99999
    return "NO"

n=int(input())
for _ in range(n):
    x=int(input())
    b=input()
    b=b.split()
    nums=[int(item) for item in b]
    ans=function(nums)
    print(ans,end="\n")


