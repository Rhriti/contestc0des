l=[1,2,4,7]
payb=[8,3,5,9]
arr=[]
for i in range(len(l)):arr.append([l[i],payb[i]])
arr.sort()
print(arr)
s=-1;e=0;c=1
for i in range(len(arr)):
    if arr[i][0]>e:
        c+=1
        e=arr[i][1]
    else:
        if arr[i][1]<e:
            e=arr[i][1]
print('ans',c-1)
