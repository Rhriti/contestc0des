import math
for _ in range(int(input())):
    r,c=map(int,input().split())
    d=r*c
    arr=[]
    s=1

    if r==4:
        for row in range(1,5):
            for cow in range(row,row+4*(c-1)+1,4):
                print(cow,end=' ')
            print()

    else:
        for _ in range(int(math.ceil(r/2))):
            temp=[]
            for _ in range(c):
                temp.append(s)
                s+=1
            arr.append(temp)
            s=arr[-1][0]+2*c
        s=1+c
        for _ in range(int(r-math.ceil(r/2))):
            temp=[]
            for _ in range(c):
                temp.append(s)
                s+=1
            arr.append(temp)
            s=arr[-1][0]+2*c
    
        for row in range(len(arr)):
            for cow in range(len(arr[0])):
                print(arr[row][cow],end=' ')
            print()



            

