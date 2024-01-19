import heapq as hq
class Solution:
    def leftmostBuildingQueries(self,height , que ) :
        arr=[-1 for _ in range(len(que))]
        newq=[]
        for index,ele in enumerate(que):
            if ele[0]==ele[1]:arr[index]=ele[0]
            elif height[max(ele[0],ele[1])]>height[min(ele[0],ele[1])]:
                arr[index]=max(ele[1],ele[0])
            else:newq.append([max(ele[1],ele[0]),max(height[ele[0]],height[ele[1]]),index])

        hq.heapify(newq)
        print(arr)
        print(newq)
        for index,hei in enumerate(height):
            while newq and newq[0][0]<index and hei>newq[0][1]:
                print('wtf')
                out=hq.heappop(newq)
                arr[out[2]]=index
        
        for i in range(len(que)):
            print(que[i],arr[i])
          
s=Solution()
print(s.leftmostBuildingQueries([4,2,1,3],
[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]))