from grid import *
from gridInit import *
from tfsf import *
from ezinc import *
from update import *
from snapshot import *
from abc import *

g1 = Grid
g2 = Grid
g3 = Grid

class control:  

    
    def __init__(self,dimensions, gridInit, tfsf, abc, snapshot, update ,sourceFunction):
        self.dimensions = dimensions
        self.gridInit = gridInit
        self.tfsf = tfsf
        self.abc = abc
        self.snapshot = snapshot
        self.update = update
        self.sourceFunction = sourceFunction
    
    def initialize(self):
        
        if self.dimensions == 1:
            g1 = self.gridInit.initialize()
            self.tfsf.initialize(g1)
            self.abc.initialize(g1)
            self.snapshot.initialize(g1)
            
        
        
        elif self.dimensions == 2:
            g2 = self.gridInit.initialize()
            self.tfsf.initialize(g2)
            self.abc.initialize(g2)
            self.snapshot.initialize(g2)
            
        
        if self.dimensions == 3:
            g3 = self.gridInit.initialize()
            self.tfsf.initialize(g3)
            self.abc.initialize(g3)
            self.snapshot.initialize(g3)
        
        
    

    def iterate(maxTime):

        for t in range(maxTime):
            
            if self.dimensions == 1:
                g1.time = t
                self.update.magneticField(g1)
                self.abc.apply(g1)
                self.update.electricField(g1)
                self.tfsf.update(g1)
                self.sourceFunction.apply(float(g1.time),  0.0)
                self.snapshot.snap(g1)
            

            elif self.dimensions == 2:
                g2.time = t
                self.update.magneticField(g2)
                self.abc.apply(g2)
                self.update.electricField(g2)
                self.tfsf.update(g2)
                self.sourceFunction.apply( float(g2.time),  0.0)
                self.snapshot.snap(g2)
            

            else:
                g3.time = t
                self.update.magneticField(g3)
                self.abc.apply(g3)
                self.update.electricField(g3)
                self.tfsf.update(g3)
                self.sourceFunction.apply( float(g3.time),  0.0)
                self.snapshot.snap(g3)
            
            print(ez1)
        

def create_remote() :
    
    gridInit = GridInit()
    tfsf = TotalFieldScatteringField()
    abc = AbsorbingBoundaryCondition()
    snapshot = Snapshot()
    update = UpdateFunction()
    sourceFunction =  SourceFunction()
    Type = 0 

    print("Enter dimensions of grid")
    dimensions = intInput()
    if dimensions == 1:
        
        tfsf = plain1Dtfsf
        
        print("1 - absorbing boundary condition, 0 - reflection")
        boundaryType = intInput()

        if boundaryType == 1:
            abc = plain1Dabc()
        

        else:
            abc = emptyAbc()
        
        
        gridInit = plain1DGridInit()
        update = oneDUpdate()
        sourceFunction = ezInc()
    

    elif dimensions == 2 :

        print("1 - tmz, 2 - tez")
        type2D = intInput()

        if type2D == 1:
            
            Type = 1
            tfsf = tmztfsf()
            gridInit = tmzTfsfGridInit()
            update = tmzUpdate()
            abc = tmzabc()
        

        else:
            Type = 2
            tfsf = teztfsf()
            gridInit = tezGridInit()
            update = tezUpdate()
            abc = tezabc()
        

        print("1 - absorbing boundary condition, 0 - reflection")
        boundaryType = intInput()

        if boundaryType == 0:
            abc = emptyAbc()
        
        
        sourceFunction = Ricker2D()
    
    else:

        print("1 - normal, 0 - sphere")
        type3D = intInput()
        

        tfsf = tfsf3d()
        update = update3D()
        abc = abc3d()
        
        if type3D == 1:
            gridInit = GridInit3D(false) 
        
        else:
            gridInit = GridInit3D(true) 
        
        
        print("1 - absorbing boundary condition, 0 - reflection")
        boundaryType = intInput()

        if boundaryType == 0:
            abc =  emptyAbc()
        
        
        sourceFunction = Ricker2D()
    
    
    print("1 - additive source 0 - tfsf? ")
    sourceInitiator = intInput()
    
    if sourceInitiator == 1:
        tfsf = emptytfsf()
        sourceFunction = additiveSourceFunction()
    


    return control(dimensions,  gridInit,  tfsf,  abc, snapshot,  update,  sourceFunction)


def runSimulation():

    ben = create_remote()
    ben.initialize()
    ben.iterate(450)


runSimulation()