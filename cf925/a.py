
for _ in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(ord('a'),ord('z')+1):
        for j in range(ord('a'),ord('z')+1):
            for z in range(ord('a'),ord('z')+1):
                if i+j+z-3*96==n:
                    arr.append(chr(i)+chr(j)+chr(z))
    arr.sort()
    print(arr[0])