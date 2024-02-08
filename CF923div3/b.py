import heapq as hq
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    arr=[[0,ele] for ele in 'abcdefghijklmnopqrstuvwxyz']
    final=''

    for ele in s:
        for ch in arr:
            if ch[0]==ele:
                final+=ch[1]
                ch[0]+=1
                break
    
    print(final)
            
            