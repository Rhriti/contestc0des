v=set()
n=12
for i in range(1,n+1):
    #base
    if i in v:
        break
    if n%i==0:
        v.add(i)
        v.add(n//i)
print(v)
