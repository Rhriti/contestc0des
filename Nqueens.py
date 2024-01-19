import copy
class Solution:
    def solveNQueens(self, n ) :
        final=[]
        ans=[None]*n
        # row=set()
        col=set()
        dig=set()
        def NQ(i):
            if i==n:
                print('ans',ans)
                final.append(copy.deepcopy(ans))
                return
            
            for index in range(n):

                if index not in col and (i,index) not in dig:
                    col.add(index)
                    r=i
                    c=index
                    while r<n and c<n:
                        dig.add((r,c))
                        r+=1
                        c+=1
                    r=i
                    c=index
                    while 0<=r<n and 0<=c:
                        dig.add((r,c))
                        r+=1
                        c-=1
                    ans[i]=index #important
                    NQ(i+1)
                    ans[i]=None

                    col.remove(index)
                    r=i
                    c=index
                    while r<n and c<n:
                        try:
                            dig.remove((r,c))
                        except:
                            pass
                        r+=1
                        c+=1
                    r=i+1
                    c=index-1
                    while 0<=r<n and 0<=c:
                        try:
                            dig.remove((r,c))
                        except:
                            pass
                        r+=1
                        c-=1

        NQ(0)
        order=[]
        for ele in final:
            ans=[['.' for _ in range(n)] for _ in range(n)]
            for  i in range(n):
                ans[i][ele[i]]='Q'
            order.append(copy.deepcopy(ans))
        return order

                                

            
            
            
        