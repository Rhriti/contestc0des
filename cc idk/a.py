# cook your dish here
from collections import deque
for _ in range(int(input())):
    n=int(input())
    ans=s=input()
    for i in range(n-2):
        if s[i]=='1':
            ans='0'*(i)+'1'+'0'*(n-i-1)
            break
    print(ans)
            
