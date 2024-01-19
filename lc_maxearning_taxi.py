
def m(n , rides ) :
    #that's a plane dp problem
    rides.sort(key= lambda x:x[1])
    def dp(i):
        if i<0:
            return 0
        
        return max(dp(i-1),rides[i][1]-rides[i][0]+rides[i][2]+dp(rides[i][0]))
    return dp(len(rides)-1)

print(m(5,
[[2,5,4],[1,5,1]]))
    