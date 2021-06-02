
temporalStride = -2
frame = 0
startTime = 0
startNodeX = 0
endNodeX = 0
spatialStrideX = 0
startNodeY = 0 
endNodeY = 0
spatialStrideY = 0
startNodeZ = 0
endNodeZ = 0


class Snapshot:
    
    def initialize(g) :
        
        startTime = 0
        temporalStride = 1
        startNodeX = 0
        startNodeY = 0
        endNodeX = 20
        endNodeY = 20
        startNodeZ = 0
        endNodeZ = 15
        spatialStrideX = 1
        spatialStrideY = 1
    

    def snap(g) :
        return
    """        
        if g.type == 2:
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                for mm in range(startNodeX,endNodeX) :
                    for nn in range(startNodeY,endNodeY) :
                        print(ez[mm][nn])
           
        

        elif g.type == 3:
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                for mm in range(startNodeX,endNodeX) :
                    for nn in range(startNodeY,endNodeY) :
                        print((hz[mm][nn])
                    
        
            
        elif (g.type == 4 or g.type == 5) :
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                
                for mm in range(startNodeX,endNodeX) :
                    for nn in range(startNodeY,endNodeY):
                        for pp in range(startNodeZ,endNodeZ):
                            print(ex3[mm][nn][pp])
                        
        
        
        else:
            for mm in range(startNodeX,endNodeX):
                print(ez1[mm])
        
    

"""