n=int(input())
arr=[[None for _ in range(n)] for _ in range(n)]
if n%2==1:
    print(-1)
else:
    count=n
    path=[]
    for c in range(n):
        path.append("R")
        arr[0][c]=count%n 
        count+=1
    path.pop()
 
    for r in range(1,n):
        path.append('D')
        arr[r][c]=count%n
        count+=1
    path.append('L')
   

    for c in range(n-2,0,-1):
        if c%2==0:
            for r in range(n-1,0,-1):
                path.append('U')
                arr[r][c]=count%n
                count+=1
            path.pop()
        
        else:
            for r in range(1,n):
                path.append('D')
                arr[r][c]=count%n
                count+=1
            path.pop()
 
        path.append('L')

    for r in range(n-1,-1,-1):
        path.append('U')
        arr[r][0]=count%n
        count+=1
    path.pop()
    for ele in arr:
        print(*ele)
    print(''.join(path))

            
    