#merge intervals:
for _ in range(int(input())):
    n=int(input())
    g={}
    black=[]
    red=[]
    for _ in range(n):
        l,r,a,b=map(int,input().split())
        red.append((a,b))
        black.append((l,r))
        g[(l,r)]=(a,b)

    black.sort()
    red_merge=[]
    temp=[g[black[0]][0],g[black[0]][1]]
    tempb=[black[0][0],black[0][1]]
    black_merge=[]
    for ele in black:
        if tempb[0]<=ele[0]<=tempb[1]:
            tempb[1]=max(tempb[1],ele[1])
            temp[1]=max(temp[1],g[ele][1])
        else:
            red_merge.append(temp)
            black_merge.append(tempb)
            temp=[g[ele][0],g[ele][1]]
            tempb=[ele[0],ele[1]]
    red_merge.append(temp)
    black_merge.append(tempb)
    # print(f'red merge is {red_merge}')
    # print(f'blackmerge is {black_merge}')

    def find(x):
        i=0
        j=len(black_merge)-1
        curr=None
        while i<=j:
            mid=(i+j)//2
            if black_merge[mid][0]<=ele<=black_merge[mid][1]:
                curr=mid
                i=mid+1
            elif black_merge[mid][1]<ele:
                i=mid+1
            else:
                j=mid-1
        return curr

    input()
    q=list(map(int,input().split()))
    ans=[]
    for ele in q:
        index=find(ele)
        if index is None:
            ans.append(ele)
        else:
            if ele<=red_merge[index][1]:
                ans.append(red_merge[index][1])
            else:
                ans.append(ele)
    print(f'ans is {ans}')
