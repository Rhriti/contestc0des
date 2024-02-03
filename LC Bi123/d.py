
def numberOfPairs(points):
    points.sort()

    c=0
    for i in range(len(points)-1):
        
        cx=points[i][0]
        cy=points[i][1]
        
        for j in range(i+1,len(points)):
            
            tx=points[j][0]
            ty=points[j][1]
            
            # if  (cx<=tx and cy>=ty) :
            #     ct={i,j}
            #     f=True                         #no introuder
            #     for k in range(len(points)):
            #         if k not in ct:
            #             if cx<=points[k][0]<=tx and ty<=points[k][1]<=cy:f=False;break
                            
            #     if f:c+=1





    for i in range(len(points)-1):
        
        tx=points[i][0]
        ty=points[i][1]
        
        for j in range(i+1,len(points)):
    
            cx=points[j][0]
            cy=points[j][1]
            
            if  (cx<=tx and cy>=ty) :
                ct={i,j}
                f=True                         #no introuder
                for k in range(len(points)):
                    if k not in ct:
                        if cx<=points[k][0]<=tx and ty<=points[k][1]<=cy:f=False;break
                            
                if f:c+=1
   
    return c

print(numberOfPairs([[3,1],[1,3],[1,1]]))