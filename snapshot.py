
 temporalStride = -2, frame = 0, startTime = 0
 startNodeX = 0, endNodeX = 0, spatialStrideX = 0
 startNodeY = 0, endNodeY = 0, spatialStrideY = 0
 startNodeZ = 0, endNodeZ = 0


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
        
        if g.type == 2:
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                for mm in startNodeX...endNodeX :
                    for nn in startNodeY...endNodeY :
                        AppendToString(dataString: "\(ez[mm][nn]) ")
                    
                    AppendToString(dataString: "\n")
                
                AppendToString(dataString: "\n")
                
           
        

        else if g.type == 3:
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                for mm in startNodeX...endNodeX :
                    for nn in startNodeY...endNodeY :
                        AppendToString(dataString: "\(hz[mm][nn]) ")
                    
                    AppendToString(dataString: "\n")
                
                AppendToString(dataString: "\n")
            
        
            
        else if g.type == 4 or g.type == 5 :
            
            if (g.time >= startTime and
                (g.time - startTime) % temporalStride == 0) :
                
                
                for mm in startNodeX...endNodeX :
                    for nn in startNodeY...endNodeY:
                        for pp in startNodeZ...endNodeZ:
                            AppendToString(dataString: "\(ex3[mm][nn][pp]) ")
                        
                        AppendToString(dataString: "\n")
                    
                    AppendToString(dataString: "\n")
                
                AppendToString(dataString: "\n")
            
            
        
        
        else:
            for mm in startNodeX...endNodeX:
                AppendToString(dataString: "\(ez1[mm]) ")
            
            AppendToString(dataString: "\n")
        
    

