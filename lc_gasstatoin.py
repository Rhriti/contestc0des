
def canCompleteCircuit( gas , cost ):
    if len(gas)==1:
        return 0
    
    #jisme headstart sbse jayda hoga wahase shuru kreunga
    start=0
    gass=gas[0]-cost[0]
    for i in range(1,len(gas)):
        if gas[i]-cost[i]>gass:
            gass=gas[i]-cost[i]
            start=i
    if gass<0:
        return -1
    j=(start+1)%len(gas)
    
    while gass>=0 :
        #base
        if start==j:
            return start
        
        gass+=gas[j]
        if gass>=cost[j]:
            gass-=cost[j]
            j=(j+1)%len(gas)
        
        else:
            return -1
    return -1
print(canCompleteCircuit([2,3,4],[3,4,3]))
            
            
            
            
            
            
            
            
    
    