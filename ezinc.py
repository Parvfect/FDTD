
class SourceFunction:
    def initialize(g):return
    def apply(time, location):return 


class emptySourceFunction:
    
    def initialize(g):return
    
    
    def apply(time, location) :
        return 0.0
    


class ezInc(SourceFunction):

    delay = 1.2
    width = 4
    cdtds = 1.0
    ppw = 4
    sourceFunctionType = 1

    def initialize(g):
        
        self.cdtds = g.cdtds
        self.delay = 1.2
        self.width = 2
        self.ppw = 4
    

    def apply(time, location)  :
        
        if sourceFunctionType == 1:
            
            return exp(-pow((time - self.delay - location / self.cdtds) / self.width, 2))
        
            
        elif sourceFunctionType == 2:
            
            return sin(2.0 * Double.pi / Double(self.ppw) * (self.cdtds * time - location))
        

        return 0.0
    


class Ricker2D(SourceFunction) :
    
    cdtds = 0.0
    ppw = 0


    def initialize(g) :
        cdtds = g.cdtds
        self.ppw = 4
    

    def apply(time , location) :
        
        arg = 0.0
        
        arg = Double.pi * ((self.cdtds * time - location) / Double(self.ppw) - 1.0)
        arg = arg * arg
        
        
        return (1.0 - 2.0 * arg) * exp(-arg)
    


class additiveSourceFunction(SourceFunction) :

    delay = 1.2
    width = 4
    cdtds = 1.0
    ppw = 4
    sourceFunctionType = 1
    size_x = 0
    size_y = 0
    size_z = 0
    Type = 0

    def initialize(g):
        self.cdtds = g.cdtds
        self.ppw = 4
        self.delay = 1.2
        self.width = 4
        self.sourceFunctionType = 1
        self.size_x = g.size_x
        self.size_y = g.size_y
        self.size_z = g.size_z
        self.Type = g.Type
    

    def apply(time, location) :
        
        if self.Type == 1:
            ez1[self.size_x/2] += ezInc().apply(time, location)
        

        elif self.Type == 2:
            ez[self.size_x/2][self.size_y/2] += Ricker2D().apply(time, location)
        
        
        elif self.Type == 3:
            ex[self.size_x/2][self.size_y/2] += Ricker2D().apply(time, location)
        

        elif self.Type == 4:
            ez3[self.size_x/2][self.size_y/2][self.size_z/2] += Ricker2D().apply(time, location)
        
        
        else:
            
            return 0.0
    


