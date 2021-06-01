import Foundation

public protocol GridInit{
    func initialize() -> Grid
}

public struct plain1DGridInit : GridInit{
    
    let LOSS =  0.02
    let LOSS_LAYER = 180 
    let EPSR = 9.0
    
    public func initialize() -> Grid {
        
        let imp0 = 377.0
        let size_x = 200   
        let maxTime = 450 
        let cdtds = 1.0  
        
        var Ez = make1DArray(size:size_x)
        var Ceze = make1DArray(size:size_x)
        var Cezh = make1DArray(size:size_x)
        var Hy = make1DArray(size:size_x-1)
        var Chyh = make1DArray(size:size_x-1)
        var Chye = make1DArray(size:size_x-1)
        
        for mm in 0...(size_x-1){
            
            if (mm < 100) {
                Ceze[mm] = 1.0;
                Cezh[mm] = imp0;
            }
                
            else if (mm < LOSS_LAYER) {
                Ceze[mm] = 1.0;
                Cezh[mm] = imp0 / EPSR;
            }
                
            else {
                Ceze[mm] = (1.0 - LOSS) / (1.0 + LOSS);
                Cezh[mm] = imp0 / EPSR / (1.0 + LOSS);
            }
        }
        
        for mm in 0...(size_x - 2) {
            
            if (mm < LOSS_LAYER) {
                Chyh[mm] = 1.0;
                Chye[mm] = 1.0 / imp0;
                
            } else {
                Chyh[mm] = (1.0 - LOSS) / (1.0 + LOSS);
                Chye[mm] = 1.0 / imp0 / (1.0 + LOSS);
            }
            
        }
        
        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye
        
        return Grid(size_x:size_x, size_y: 0, size_z: 0,maxTime: maxTime, time:0, cdtds:cdtds, type: 1)
    }
}

public struct auxillaryHzGridInit : GridInit{
    
    var NLOSS = 20.0
    var MAX_LOSS = 0.35
    
    public func initialize() -> Grid{
        
        var imp0 = 377.0
        var depthInLayer = 0.0
        var lossFactor = 0.0
        var cdtds = 1.0
        var size_x = Int(NLOSS)
        var MaxTime = 450
        
        var Ey = make1DArray(size:size_x)
        var Ceye = make1DArray(size:size_x)
        var Ceyh = make1DArray(size:size_x)
        var Hz = make1DArray(size:size_x-1)
        var Chzh = make1DArray(size:size_x-1)
        var Chze = make1DArray(size:size_x-1)
        
        for mm in 0...(size_x - 2){
            
            if (mm < size_x - 1 - Int(NLOSS)){
                Ceye[mm] = 1.0
                Ceyh[mm] = cdtds + imp0
                Chzh[mm] = 1.0
                Chze[mm] = cdtds / imp0
                
            }
                
            else{
                depthInLayer += 0.5
                lossFactor = MAX_LOSS * pow(MAX_LOSS * 2.0, depthInLayer / Double(NLOSS))
                Ceye[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Ceyh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = MAX_LOSS  * pow(depthInLayer * 2.0, Double(NLOSS))
                Chzh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chze[mm] = cdtds / imp0 / (1.0 + lossFactor)
            }
        }
        
        ey1 = Ey
        hz1 = Hz
        ceye1 = Ceye
        ceyh1 = Ceyh
        chzh1 = Chzh
        chze1 = Chze
        
        return Grid(size_x: size_x, size_y: 0, size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    }
}
public struct auxillaryEzGridInit : GridInit{
    
    var NLOSS = 20.0
    var MAX_LOSS = 0.35
    
    public func initialize() -> Grid{
        
        var imp0 = 377.0
        var depthInLayer = 0.0
        var lossFactor = 0.0
        var cdtds = 1.0
        var MaxTime = 450
        var size_x = Int(NLOSS) 
        
        var Ez = make1DArray(size:size_x)
        var Ceze = make1DArray(size:size_x)
        var Cezh = make1DArray(size:size_x)
        var Hy = make1DArray(size:size_x-1)
        var Chyh = make1DArray(size:size_x-1)
        var Chye = make1DArray(size:size_x-1)
        
        for mm in 0...(size_x - 2){
            
            if (mm < size_x - 1 - Int(NLOSS)){
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            }else{
                depthInLayer = Double((mm - size_x - 1 - Int(NLOSS))) + 0.5
                lossFactor = pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            }
            
        }

        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye
        
        return Grid(size_x: size_x, size_y: 0 , size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    }
}


public struct aux3DGridInit : GridInit{
    
    var NLOSS = 25.0
    var MAX_LOSS = 0.35
    
    public func initialize() -> Grid{
        
        var imp0 = 377.0
        var depthInLayer = 0.0
        var lossFactor = 0.0
        var cdtds = 1.0
        var MaxTime = 450
        var size_x = Int(NLOSS) 
        
        var Ez = make1DArray(size:size_x)
        var Ceze = make1DArray(size:size_x)
        var Cezh = make1DArray(size:size_x)
        var Hy = make1DArray(size:size_x-1)
        var Chyh = make1DArray(size:size_x-1)
        var Chye = make1DArray(size:size_x-1)
        
        for mm in 0...(size_x - 2) {
            
            if (mm < size_x - 1 - Int(NLOSS)){
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            }
            else{
                depthInLayer += 0.5
                lossFactor = 0.35 * pow(depthInLayer / NLOSS, 2)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = 0.35 * pow(depthInLayer / NLOSS, 2)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            }
            
        }
        
        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye

        return Grid(size_x: size_x, size_y: 0 , size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    }
}

public struct tmzTfsfGridInit : GridInit{
    
    public func initialize() -> Grid{
        
        var imp0 = 377.0
        var size_x = 100            
        var size_y = 81             
        var maxTime = 10         
        var cdtds = 1.0 / sqrt(2.0) 
        
        var Ez = make2DArray(x:size_x, y: size_y)
        var Ceze = make2DArray(x:size_x, y: size_y)
        var Cezh = make2DArray(x:size_x, y: size_y)
        
        var Hx = make2DArray(x:size_x, y:(size_y - 1))
        var Chxh = make2DArray(x:size_x, y:(size_y - 1))
        var Chxe = make2DArray(x:size_x, y:(size_y - 1))
        
        var Hy = make2DArray(x:size_x - 1, y: size_y)
        var Chyh = make2DArray(x:size_x - 1, y: size_y)
        var Chye = make2DArray(x:size_x - 1, y: size_y)
        
        for mm in 0...size_x {
            for nn in 0...size_y{
                Ceze[mm][nn] = 1.0
                Cezh[mm][nn] = cdtds * imp0
            }
        }
        
        for mm in 0...size_x{
            for nn in 0...size_y - 1{
                Chxh[mm][nn] = 1.0
                Chxe[mm][nn] = cdtds / imp0
            }
        }
        
        for mm in 0...size_x - 1{
            for nn in 0...size_y{
                Chyh[mm][nn] = 1.0
                Chye[mm][nn] = cdtds / imp0
            }
        }
        
        ez = Ez
        hy = Hy
        hx = Hx
        ceze = Ceze
        cezh = Cezh
        chyh = Chyh
        chye = Chye
        chxh = Chxh
        chxe = Chxe
        
        return Grid(size_x: size_x, size_y: size_y, size_z: 0, maxTime: maxTime, time: 0, cdtds: cdtds, type : 2)
    }
}

public struct tezGridInit : GridInit {
    
    public func initialize() -> Grid {
        
        let imp0 = 377.0
        let size_x = 92
        let size_y = 82
        let MaxTime = 10
        let Cdtds = 1.0/sqrt(2.0)
        
        var Ex = make2DArray(x: size_x - 1, y: size_y)
        var Cexe = make2DArray(x: size_x - 1, y: size_y)
        var Cexh = make2DArray(x: size_x - 1, y: size_y)
        
        var Ey = make2DArray(x: size_x, y: size_y - 1)
        var Ceye = make2DArray(x: size_x, y: size_y - 1)
        var Ceyh = make2DArray(x: size_x, y: size_y - 1)
        
        var Hz = make2DArray(x: size_x - 1, y: size_y - 1)
        var Chzh = make2DArray(x: size_x - 1, y: size_y - 1)
        var Chze = make2DArray(x: size_x - 1, y: size_y - 1)
        
        for mm in 0...(size_x-1){
            for nn in 0...(size_y){
                Cexe[mm][nn] = 1.0
                Cexh[mm][nn] = Cdtds * imp0
            }
        }
        
        for mm in 0...(size_x){
            for nn in 0...(size_y-1){
                Ceye[mm][nn] = 1.0
                Ceyh[mm][nn] = Cdtds * imp0
            }
        }
        
        let rad = 12
        let xCenter = size_x/2
        let yCenter = size_y/2
        let r2 = rad * rad
        
        var xLocation = 0
        var yLocation = 0
        
        for mm in 1...(size_x-1){
            xLocation = mm - xCenter
            
            for nn in 1...(size_y-1){
                yLocation = nn - yCenter
                if ((xLocation * xLocation + yLocation * yLocation) < r2){
                    Cexe[mm][nn] = 0.0
                    Cexh[mm][nn] = 0.0
                    Cexe[mm][nn + 1] = 0.0
                    Ceye[mm][nn + 1] = 0.0
                    Ceye[mm + 1][nn] = 0.0
                    Ceyh[mm + 1][nn] = 0.0
                    Ceye[mm][nn] = 0.0
                    Ceyh[mm][nn] = 0.0
                }
            }
        }
        
        for mm in 0...(size_x-1){
            for nn in 0...(size_y-1){
                Chzh[mm][nn] = 1.0
                Chze[mm][nn] = Cdtds/imp0
            }
        }
        
        ex = Ex
        ey = Ey
        hz = Hz
        cexe = Cexe
        cexh = Cexh
        ceye = Ceye
        ceyh = Ceyh
        chze = Chze
        chzh = Chzh
        
        return Grid(size_x: size_x, size_y: size_y, size_z: 0, maxTime: MaxTime, time: 0, cdtds: Cdtds, type : 3)
    }
}

public struct GridInit3D : GridInit{

    var isSpherePresent : Bool
    
    public func initialize() -> Grid {
        
        let imp0 = 377.0
        let type = 5
        let size_x = 35
        let size_y = 35
        let size_z = 35
        let Maxtime = 2
        let cdtds = 1.0/sqrt(3.0)
        
        let m_c = 17
        let n_c = 17
        let p_c = 17
        let isSpherePresent:Bool
        var m2:Double
        var n2:Double
        var p2:Double
        var r2:Double
        let rad = 8.0
        
        
        var mm:Int = 0
        var nn:Int = 0
        var pp:Int = 0
        
        
        var Ex = make3DArray(x: size_x - 1, y: size_y, z: size_z)
        var Cexe = make3DArray(x: size_x - 1, y: size_y, z: size_z)
        var Cexh = make3DArray(x: size_x - 1, y: size_y, z: size_z)
        
        var Ey = make3DArray(x: size_x, y: size_y - 1, z: size_z)
        var Ceye = make3DArray(x: size_x, y: size_y - 1, z: size_z)
        var Ceyh = make3DArray(x: size_x, y: size_y - 1, z: size_z)
        
        var Ez = make3DArray(x: size_x, y: size_y, z: size_z - 1)
        var Ceze = make3DArray(x: size_x, y: size_y, z: size_z - 1)
        var Cezh = make3DArray(x: size_x, y: size_y, z: size_z - 1)
        
        var Hx = make3DArray(x: size_x, y: size_y - 1, z: size_z-1)
        var Chxh = make3DArray(x: size_x, y: size_y - 1, z: size_z - 1)
        var Chxe = make3DArray(x: size_x, y: size_y - 1, z: size_z - 1)
        
        var Hy = make3DArray(x: size_x - 1, y: size_y, z: size_z-1)
        var Chyh = make3DArray(x: size_x - 1, y: size_y, z: size_z-1)
        var Chye = make3DArray(x: size_x - 1, y: size_y, z: size_z-1)
        
        var Hz = make3DArray(x: size_x - 1, y: size_y - 1, z: size_z)
        var Chzh = make3DArray(x: size_x - 1, y: size_y - 1, z: size_z)
        var Chze = make3DArray(x: size_x - 1, y: size_y - 1, z: size_z)
        
        for mm in 0...(size_x - 1){
            for nn in 0...(size_y){
                for pp in 0...(size_z){
                    Cexe[mm][nn][pp] = 1.0
                    Cexh[mm][nn][pp] = cdtds * imp0
                }
            }
        }
        
        for mm in 0...(size_x){
            for nn in 0...(size_y - 1){
                for pp in 0...(size_z){
                    Ceye[mm][nn][pp] = 1.0
                    Ceyh[mm][nn][pp] = cdtds / imp0
                }
            }
        }
        
        for mm in 0...(size_x){
            for nn in 0...(size_y){
                for pp in 0...(size_z - 1){
                    Ceze[mm][nn][pp] = 1.0
                    Cezh[mm][nn][pp] = cdtds / imp0
                }
            }
        }
        
        if self.isSpherePresent {
            r2 = rad * rad
            
            for mm in 2...(size_x - 2){
                m2 = (Double(mm) + 0.5 - Double(m_c)) * (Double(mm) + 0.5 - Double(n_c))
                
                for nn in 2...(size_y - 2){
                    n2 = (Double(nn) + 0.5 - Double(m_c)) * (Double(nn) + 0.5 - Double(n_c))
                    
                    for pp in 2...(size_z - 2){
                        p2 = (Double(pp) + 0.5 - Double(p_c)) * (Double(pp) + 0.5 - Double(p_c))
                        
                        if (m2+n2+p2<r2){
                            
                            Cexe[mm][nn][pp] = 0.0
                            Cexe[mm][nn+1][pp] = 0.0
                            Cexe[mm][nn][pp + 1] = 0.0
                            Cexe[mm][nn + 1][pp + 1] = 0.0
                            Cexh[mm][nn][pp] = 0.0
                            Cexh[mm][nn + 1][pp] = 0.0
                            Cexh[mm][nn][pp + 1] = 0.0
                            Cexh[mm][nn + 1][pp + 1] = 0.0
                            
                            Ceye[mm][nn][pp] = 0.0
                            Ceye[mm+1][nn][pp] = 0.0
                            Ceye[mm][nn][pp+1] = 0.0
                            Ceye[mm+1][nn][pp+1] = 0.0
                            Ceyh[mm][nn][pp] = 0.0
                            Ceyh[mm+1][nn][pp] = 0.0
                            Ceyh[mm][nn][pp+1] = 0.0
                            Ceyh[mm+1][nn][pp+1] = 0.0
                            
                            Ceze[mm][nn][pp] = 0.0
                            Ceze[mm+1][nn][pp] = 0.0
                            Ceze[mm][nn+1][pp] = 0.0
                            Ceze[mm+1][nn+1][pp] = 0.0
                            Cezh[mm][nn][pp] = 0.0
                            Cezh[mm+1][nn][pp] = 0.0
                            Cezh[mm][nn+1][pp] = 0.0
                            Cezh[mm+1][nn+1][pp] = 0.0
                        }
                    }
                }
            }
        }
        
        
        for mm in 0...(size_x){
            for nn in 0...(size_y - 1){
                for pp in 0...(size_z - 1){
                    Chxh[mm][nn][pp] = 1.0
                    Chxe[mm][nn][pp] = cdtds / imp0
                }
            }
        }
        
        for mm in 0...(size_x - 1){
            for nn in 0...(size_y){
                for pp in 0...(size_z - 1){
                    Chyh[mm][nn][pp] = 1.0
                    Chye[mm][nn][pp] = cdtds / imp0
                }
            }
        }
        
        for mm in 0...(size_x - 1){
            for nn in 0...(size_y - 1){
                for pp in 0...(size_z){
                    Chzh[mm][nn][pp] = 1.0
                    Chze[mm][nn][pp] = cdtds / imp0
                }
            }
        }
        
        ex3 = Ex
        cexe3 = Cexe
        cexh3 = Cexh
        
        ey3 = Ey
        ceye3 = Ceye
        ceyh3 = Ceyh
        
        ez3 = Ez
        ceze3 = Ceze
        cezh3 = Cezh
        
        hx3 = Hx
        chxh3 = Chxh
        chxe3 = Chxe
        
        hy3 = Hy
        chyh3 = Chyh
        chye3 = Chye
        
        hz3 = Hz
        chzh3 = Chzh
        chze3 = Chze
        
        return Grid(size_x:size_x, size_y: size_y, size_z: size_z, maxTime: Maxtime,time:0, cdtds:cdtds, type: 4)
    }
}

