import Foundation

public protocol SourceFunction{
    mutating func initialize(g : Grid)
    func apply(time : Double, location : Double) -> Double
}

public struct emptySourceFunction{
    
    public mutating func initialize(g : Grid){
    }
    
    public func apply(time : Double, location : Double) -> Double{
        return 0.0
    }
}

public struct ezInc : SourceFunction{

    var delay:Double = 1.2
    var width:Double = 4
    var cdtds:Double = 1.0
    var ppw:Double = 4
    var sourceFunctionType = 1

    public mutating func initialize(g : Grid){
        
        self.cdtds = g.cdtds;
        self.delay = 1.2
        self.width = 2
        self.ppw = 4
    }

    public func apply(time : Double, location : Double) -> Double {
        
        if sourceFunctionType == 1{
            
            return exp(-pow((time - self.delay - location / self.cdtds) / self.width, 2))
        }
            
        else if sourceFunctionType == 2{
            
            return sin(2.0 * Double.pi / Double(self.ppw) * (self.cdtds * time - location))
        }

        return 0.0
    }
}

public struct Ricker2D : SourceFunction {
    
    var cdtds = 0.0
    var ppw = 0


    public mutating func initialize(g: Grid) {
        cdtds = g.cdtds
        self.ppw = 4
    }

    public func apply(time: Double , location: Double) -> Double{
        
        var arg = 0.0
        
        arg = Double.pi * ((self.cdtds * time - location) / Double(self.ppw) - 1.0)
        arg = arg * arg
        
        
        return (1.0 - 2.0 * arg) * exp(-arg)
    }
}

public struct additiveSourceFunction : SourceFunction {

    var delay:Double = 1.2
    var width:Double = 4
    var cdtds:Double = 1.0
    var ppw:Double = 4
    var sourceFunctionType = 1
    var size_x = 0
    var size_y = 0
    var size_z = 0
    var type = 0

    public mutating func initialize(g : Grid){
        self.cdtds = g.cdtds
        self.ppw = 4
        self.delay = 1.2
        self.width = 4
        self.sourceFunctionType = 1
        self.size_x = g.size_x
        self.size_y = g.size_y
        self.size_z = g.size_z
        self.type = g.type
    }

    public func apply(time : Double, location : Double) -> Double{
        
        if self.type == 1{
            ez1[self.size_x/2] += ezInc().apply(time : time, location : location)
        }

        else if self.type == 2{
            ez[self.size_x/2][self.size_y/2] += Ricker2D().apply(time : time, location : location)
        }
        
        else if self.type == 3{
            ex[self.size_x/2][self.size_y/2] += Ricker2D().apply(time : time, location : location)
        }

        else if self.type == 4{
            ez3[self.size_x/2][self.size_y/2][self.size_z/2] += Ricker2D().apply(time : time, location : location)
        }
        
        else{
            
        }
        
        return 0.0
    }
}

