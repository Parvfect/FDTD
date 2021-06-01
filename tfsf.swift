import Foundation

public protocol TotalFieldScatteringField{
    mutating func initialize(g : Grid)
    func update(g : Grid)
}

public struct emptytfsf : TotalFieldScatteringField{
    public mutating func initialize(g : Grid){}
    public func update(g : Grid){}
}

public struct teztfsf : TotalFieldScatteringField {

    var firstX = 0
    var firstY = 0

    var lastX = 0
    var lastY = 0
    
    var aux_grid = auxillaryHzGridInit().initialize()
    
    public mutating func initialize(g : Grid) {
    
        firstX = 2
        firstY = 22
        lastX = 5
        lastY = 62
        g1 = aux_grid
    }

    public func update(g : Grid){
        
        var mm = 0
        var nn = 0
        
        if (firstX <= 0) {
            print("tfsfUpdate: tfsfInit must be called before tfsfUpdate. Boundary location must be set to positive value.\n")
        }
        
        mm = firstX - 1
        for nn in firstY...lastY{
            hz[mm][nn] += chze[mm][nn] * ey1[mm + 1]
        }
        
        mm = lastX
        for nn in firstY...lastY{
            hz[mm][nn] -= chze[mm][nn] * ey1[mm]
        }
        
        
        tezUpdate().magneticField(g : g1)    
        tezUpdate().electricField(g : g1)    
        ey1[0] = ezInc().apply(time: Double(g1.time) ,location: 0.0)
        g1.time += 1    
        
        
        nn = firstY
        for mm in firstX...lastX{
            ex[mm][nn] -= cexh[mm][nn] * hz1[mm]
        }
        
        nn = lastY
        for mm in firstX...lastX{
            ex[mm][nn] += cexh[mm][nn] * hz1[mm]
        }
        
        mm = firstX
        for nn in firstY...lastY{
            ey[mm][nn] += ceyh[mm][nn] * hz1[mm - 1]
        }
        
        mm = lastX
        for nn in firstY...lastY{
            ey[mm][nn] -= ceyh[mm][nn] * hz1[mm]
        }
    }
}


public struct tmztfsf : TotalFieldScatteringField {
    
    var firstX = 0
    var firstY = 0
    var lastX = 0
    var lastY = 0

    var aux_grid = auxillaryEzGridInit().initialize()

    public mutating func initialize(g : Grid) {
        
        firstX = 2
        firstY = 5
        lastX = 2
        lastY = 10
        g1 = aux_grid
    }

    public func update(g : Grid){
        
        var mm = 0
        var nn = 0
        
        if (firstX <= 0) {
            print("tfsfUpdate: tfsfInit must be called before tfsfUpdate. Boundary location must be set to positive value.\n")
        }
        
        mm = firstX - 1
        for nn in firstY...lastY{
            
            hy[mm][nn] -= chye[mm][nn] * ez1[mm + 1]
        }
        
        mm = lastX
        for nn in firstY...lastY{
            hy[mm][nn] += chye[mm][nn] * ez1[mm]
        }
        
        nn = firstY - 1
        for mm in firstX...lastX{
            hx[mm][nn] += chxe[mm][nn] * ez1[mm]
        }
        
        nn = lastY
        for mm in firstX...lastX{
            hx[mm][nn] -= chxe[mm][nn] * ez1[mm]
        }
        
        tmzUpdate().magneticField(g : g1)   
        tmzUpdate().electricField(g : g1)   
        ez1[0] = ezInc().apply(time: Double(g1.time) ,location: 0.0) 
        g1.time += 1    
        
        mm = firstX
        for nn in firstY...lastY{
            ez[mm][nn] -= cezh[mm][nn] * hy1[mm - 1]
        }
        
        mm = lastX
        for nn in firstY...lastY{
            ez[mm][nn] += cezh[mm][nn] * hy1[mm]
    }
}
}

public struct plain1Dtfsf : TotalFieldScatteringField {
    
    var tfsfBoundary: Int = 0
    var ezIncFunc = ezInc()

    public mutating func initialize(g : Grid) {
        
        tfsfBoundary = 10
        ezIncFunc.initialize(g : g)    
    }
    
    public func update(g : Grid) {
        
        if (tfsfBoundary <= 0) {
            print("ERROR : Boundary location must be set to a positive value")
        }
        
        hy1[tfsfBoundary] -= ezIncFunc.apply(time : Double(g1.time), location:0.0) * chye1[tfsfBoundary]
        
        ez1[tfsfBoundary + 1] += ezIncFunc.apply(time : (Double(g1.time) + 0.5) , location : -0.5)
    }
}


public struct tfsf3d : TotalFieldScatteringField {
    
    var firstX = 10
    var firstY = 10
    var firstZ = 10
    var lastX = 20
    var lastY = 20
    var lastZ = 20

    var aux_grid = aux3DGridInit().initialize() 

    public mutating func initialize(g : Grid) {
        g1 = aux_grid
    }
    
    public func update(g : Grid) {
        
        var mm = 0, nn = 0, pp = 0
        
        if (firstX <= 0){
        print("tfsf: tfsfInit must be called before tfsfUpdate.\nBoundary location must be set to positive value.\n")
        }
    
        mm = firstX
        for nn in firstY...lastY{
            for pp in firstZ...lastZ{
                hy3[mm-1][nn][pp] -= chye3[mm][nn][pp] * ez1[mm]
            }
        }
    
        mm = lastX
        for nn in firstY...lastY{
            for pp in firstZ...lastZ{
                hy3[mm][nn][pp] += chye3[mm][nn][pp] * ez1[mm]
            }
        }
    
        nn = firstY
        for mm in firstX...lastX{
            for pp in firstZ...lastZ{
                hx3[mm][nn-1][pp] += chxe3[mm][nn-1][pp] * ez1[mm]
            }
        }
    
        nn = lastY
        for mm in firstX...lastX{
            for pp in firstZ...lastZ{
                hx3[mm][nn][pp] -= chxe3[mm][nn][pp] * ez1[mm]
            }
        }
    
        update3D().magneticField(g:g1)
        update3D().electricField(g:g1)
        ez1[0] = Ricker2D().apply(time : Double(g1.time), location : 0.0)
        g1.time += 1

        mm = firstX
        for nn in firstY...lastY{
            for pp in firstZ...lastZ{
                ez3[mm][nn][pp] -= cezh3[mm][nn][pp] * hy1[mm-1]
            }
        }
        mm = lastX
        for nn in firstY...lastY{
            for pp in firstZ...lastZ{
                ez3[mm][nn][pp] += cezh3[mm][nn][pp] * hy1[mm]
            }
        }
        pp = firstZ
        for mm in firstX...lastX{
            for nn in firstY...lastY{
                ex3[mm][nn][pp] += cexh3[mm][nn][pp] * hy1[mm]
            }
        }
        pp = lastZ
        for mm in firstX...lastX{
            for nn in firstY...lastY{
                ex3[mm][nn][pp] -= cexh3[mm][nn][pp] * hy1[mm]
            }
        }

    }
}

