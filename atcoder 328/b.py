n=int(input())
arr=list(input().split())
count=0
for i in range(1,n+1):

    if i<10:
        print(set(arr[i-1]))
        if len(arr[i-1])==1 and i<=int(arr[i-1]) and f'{i}' in set(arr[i-1]):
            count+=1  
        if len(arr[i-1])==2 and f'{i}' in set(arr[i-1]):
            count+=1
            if (10*i+i) <=int(arr[i-1]) and f'{10*i+i}' in  set(arr[i-1]):count+=1
        if len(arr[i-1])==3:
            if f'{i}' in set(arr[i-1]):count+=1
            if f'{10*i+i}' in set(arr[i-1]):count+=1

    elif 10<=i<=99:
        # if len(arr[i-1])==1:
        #     pass
        if len(arr[i-1])==2:
            if i<=int(arr[i-1]) and f'{i}' in set(arr[i-1]):count+=1

        if len(arr[i-1])==3 and f'{i}' in set(arr[i-1]):
            count+=1
    else:
        if arr[i-1]=='100' and f'{i}' in set(arr[i-1]):count+=1


print('ans',count)
