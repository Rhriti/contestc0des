n=44
ans=set()
for divi in range(2,44+1):
    while n%divi==0:
        n=n/divi
        ans.add(divi)
print(ans)

#above time complexity is O(n) we need smaller time complexity
import math
n=44
ans1=set()
for divi in range(2,int(math.sqrt(n))+1):
    while n%divi==0:
        n=n/divi
        ans1.add(divi)
if n!=1:
    ans1.add(int(n))
print(ans1)

    

