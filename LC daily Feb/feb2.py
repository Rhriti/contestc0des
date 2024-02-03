s='123456789'
arr=[]
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        arr.append(int(s[i:j+1]))
arr.sort()
print(arr)