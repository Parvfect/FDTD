import Foundation

class TotalFieldScatteringField:
     def  initialize(g)
    def  update(g)


class emptytfsf (TotalFieldScatteringField):
     def  initialize(g):
    def  update(g):


class teztfsf (TotalFieldScatteringField) :

    firstX = 0
    firstY = 0

    lastX = 0
    lastY = 0
    
    aux_grid = auxillaryHzGridInit().initialize()
    
     def  initialize(g) :
    
        firstX = 2
        firstY = 22
        lastX = 5
        lastY = 62
        g1 = aux_grid
    

    def  update(g):
        
        mm = 0
        nn = 0
        
        if (firstX <= 0) :
            print("tfsfUpdate: tfsfInit must be called before tfsfUpdate. Boundary location must be set to positive value.\n")
        
        
        mm = firstX - 1
        for nn in range(firstY,lastY):
            hz[mm][nn] += chze[mm][nn] * ey1[mm + 1]
        
        
        mm = lastX
        for nn in range(firstY,lastY):
            hz[mm][nn] -= chze[mm][nn] * ey1[mm]
        
        
        
        tezUpdate().magneticField(g1)    
        tezUpdate().electricField(g1)    
        ey1[0] = ezInc().apply(Double(g1.time) , 0.0)
        g1.time += 1    
        
        
        nn = firstY
        for mm in range(firstX,lastX):
            ex[mm][nn] -= cexh[mm][nn] * hz1[mm]
        
        
        nn = lastY
        for mm in range(firstX,lastX):
            ex[mm][nn] += cexh[mm][nn] * hz1[mm]
        
        
        mm = firstX
        for nn in range(firstY,lastY):
            ey[mm][nn] += ceyh[mm][nn] * hz1[mm - 1]
        
        
        mm = lastX
        for nn in range(firstY,lastY):
            ey[mm][nn] -= ceyh[mm][nn] * hz1[mm]
        
    



class tmztfsf (TotalFieldScatteringField) :
    
    firstX = 0
    firstY = 0
    lastX = 0
    lastY = 0

    aux_grid = auxillaryEzGridInit().initialize()

     def  initialize(g) :
        
        firstX = 2
        firstY = 5
        lastX = 2
        lastY = 10
        g1 = aux_grid
    

    def  update(g):
        
        mm = 0
        nn = 0
        
        if (firstX <= 0) :
            print("tfsfUpdate: tfsfInit must be called before tfsfUpdate. Boundary location must be set to positive value.\n")
        
        
        mm = firstX - 1
        for nn in range(firstY,lastY):
            
            hy[mm][nn] -= chye[mm][nn] * ez1[mm + 1]
        
        
        mm = lastX
        for nn in range(firstY,lastY):
            hy[mm][nn] += chye[mm][nn] * ez1[mm]
        
        
        nn = firstY - 1
        for mm in range(firstX,lastX):
            hx[mm][nn] += chxe[mm][nn] * ez1[mm]
        
        
        nn = lastY
        for mm in range(firstX,lastX):
            hx[mm][nn] -= chxe[mm][nn] * ez1[mm]
        
        
        tmzUpdate().magneticField(g : g1)   
        tmzUpdate().electricField(g : g1)   
        ez1[0] = ezInc().apply(time: Double(g1.time) ,location: 0.0) 
        g1.time += 1    
        
        mm = firstX
        for nn in range(firstY,lastY):
            ez[mm][nn] -= cezh[mm][nn] * hy1[mm - 1]
        
        
        mm = lastX
        for nn in range(firstY,lastY):
            ez[mm][nn] += cezh[mm][nn] * hy1[mm]
    



class plain1Dtfsf (TotalFieldScatteringField) :
    
    tfsfBoundary: Int = 0
    ezIncdef  = ezInc()

     def  initialize(g) :
        
        tfsfBoundary = 10
        ezIncdef .initialize(g : g)    
    
    
    def  update(g) :
        
        if (tfsfBoundary <= 0) :
            print("ERROR : Boundary location must be set to a positive value")
        
        
        hy1[tfsfBoundary] -= ezIncdef .apply(time : Double(g1.time), location:0.0) * chye1[tfsfBoundary]
        
        ez1[tfsfBoundary + 1] += ezIncdef .apply(time : (Double(g1.time) + 0.5) , location : -0.5)
    



class tfsf3d (TotalFieldScatteringField) :
    
    firstX = 10
    firstY = 10
    firstZ = 10
    lastX = 20
    lastY = 20
    lastZ = 20

    aux_grid = aux3DGridInit().initialize() 

     def  initialize(g) :
        g1 = aux_grid
    
    
    def  update(g) :
        
        mm = 0, nn = 0, pp = 0
        
        if (firstX <= 0):
        print("tfsf: tfsfInit must be called before tfsfUpdate.\nBoundary location must be set to positive value.\n")
        
    
        mm = firstX
        for nn in range(firstY,lastY):
            for pp in range(firstZ,lastZ):
                hy3[mm-1][nn][pp] -= chye3[mm][nn][pp] * ez1[mm]
            
        
    
        mm = lastX
        for nn in range(firstY,lastY):
            for pp in range(firstZ,lastZ):
                hy3[mm][nn][pp] += chye3[mm][nn][pp] * ez1[mm]
            
        
    
        nn = firstY
        for mm in range(firstX,lastX):
            for pp in range(firstZ,lastZ):
                hx3[mm][nn-1][pp] += chxe3[mm][nn-1][pp] * ez1[mm]
            
        
    
        nn = lastY
        for mm in range(firstX,lastX):
            for pp in range(firstZ,lastZ):
                hx3[mm][nn][pp] -= chxe3[mm][nn][pp] * ez1[mm]
            
        
    
        update3D().magneticField(g1)
        update3D().electricField(g1)
        ez1[0] = Ricker2D().apply(Double(g1.time), 0.0)
        g1.time += 1

        mm = firstX
        for nn in range(firstY,lastY):
            for pp in range(firstZ,lastZ):
                ez3[mm][nn][pp] -= cezh3[mm][nn][pp] * hy1[mm-1]
            
        
        mm = lastX
        for nn in range(firstY,lastY):
            for pp in range(firstZ,lastZ):
                ez3[mm][nn][pp] += cezh3[mm][nn][pp] * hy1[mm]
            
        
        pp = firstZ
        for mm in range(firstX,lastX):
            for nn in range(firstY,lastY):
                ex3[mm][nn][pp] += cexh3[mm][nn][pp] * hy1[mm]
            
        
        pp = lastZ
        for mm in range(firstX,lastX):
            for nn in range(firstY,lastY):
                ex3[mm][nn][pp] -= cexh3[mm][nn][pp] * hy1[mm]
            
        

    


