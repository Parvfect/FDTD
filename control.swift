public var g1 = Grid()
public var g2 = Grid()
public var g3 = Grid()

public struct control{  

    var dimensions : Int
    var gridInit : GridInit
    var tfsf: TotalFieldScatteringField
    var abc : AbsorbingBoundaryCondition
    var snapshot : Snapshot
    var update : UpdateFunction
    var sourceFunction : SourceFunction

    public mutating func initialize(){
        
        if self.dimensions == 1{
            g1 = self.gridInit.initialize()
            self.tfsf.initialize(g : g1)
            self.abc.initialize(g : g1)
            self.snapshot.initialize(g : g1)
            
        }
        
        else if self.dimensions == 2{
            g2 = self.gridInit.initialize()
            self.tfsf.initialize(g : g2)
            self.abc.initialize(g : g2)
            self.snapshot.initialize(g : g2)
            
        }
        if self.dimensions == 3{
            g3 = self.gridInit.initialize()
            self.tfsf.initialize(g : g3)
            self.abc.initialize(g : g3)
            self.snapshot.initialize(g : g3)
        }
        
    }

    public mutating func iterate(maxTime: Int){

        for t in 0...maxTime{
            
            if self.dimensions == 1{
                g1.time = t
                self.update.magneticField(g : g1)
                self.abc.apply(g : g1)
                self.update.electricField(g : g1)
                self.tfsf.update(g : g1)
                self.sourceFunction.apply(time : Double(g1.time), location : 0.0)
                self.snapshot.snap(g : g1)
            }

            else if self.dimensions == 2{
                g2.time = t
                self.update.magneticField(g : g2)
                self.abc.apply(g : g2)
                self.update.electricField(g : g2)
                self.tfsf.update(g : g2)
                self.sourceFunction.apply(time : Double(g2.time), location : 0.0)
                self.snapshot.snap(g : g2)
            }

            else{
                g3.time = t
                self.update.magneticField(g : g3)
                self.abc.apply(g : g3)
                self.update.electricField(g : g3)
                self.tfsf.update(g : g3)
                self.sourceFunction.apply(time : Double(g3.time), location : 0.0)
                self.snapshot.snap(g : g3)
            }
           
        }
        
        writeToFile(FileURL: "dataFile", dataToWrite: DataString)
    }
}

public func create_remote() -> control{
    
    var gridInit : GridInit
    var tfsf: TotalFieldScatteringField
    var abc : AbsorbingBoundaryCondition
    var snapshot = Snapshot()
    var update : UpdateFunction
    var sourceFunction : SourceFunction
    var type : Int

    print("Enter dimensions of grid")
    let dimensions = intInput()
    if dimensions == 1{
        
        tfsf = plain1Dtfsf() as TotalFieldScatteringField
        
        print("1 - absorbing boundary condition, 0 - reflection")
        let boundaryType = intInput()

        if boundaryType == 1{
            abc = plain1Dabc() as AbsorbingBoundaryCondition
        }

        else{
            abc = emptyAbc() as AbsorbingBoundaryCondition
        }
        
        gridInit = plain1DGridInit() as GridInit
        update = oneDUpdate() as UpdateFunction
        sourceFunction = ezInc() as SourceFunction
    }

    else if dimensions == 2 {

        print("1 - tmz, 2 - tez")
        let type2D = intInput()

        if type2D == 1{
            
            type = 1
            tfsf = tmztfsf() as TotalFieldScatteringField
            gridInit = tmzTfsfGridInit() as GridInit
            update = tmzUpdate() as UpdateFunction
            abc = tmzabc() as AbsorbingBoundaryCondition
        }

        else{
            type = 2
            tfsf = teztfsf() as TotalFieldScatteringField
            gridInit = tezGridInit() as GridInit
            update = tezUpdate() as UpdateFunction
            abc = tezabc() as AbsorbingBoundaryCondition
        }

        print("1 - absorbing boundary condition, 0 - reflection")
        let boundaryType = intInput()

        if boundaryType == 0{
            abc = emptyAbc() as AbsorbingBoundaryCondition
        }
        
        sourceFunction = Ricker2D() as SourceFunction
    }
    else{

        print("1 - normal, 0 - sphere")
        let type3D = intInput()
        

        tfsf = tfsf3d() as TotalFieldScatteringField
        update = update3D() as UpdateFunction
        abc = abc3d() as AbsorbingBoundaryCondition
        
        if type3D == 1{
            gridInit = GridInit3D(isSpherePresent : false) as GridInit
        }
        else{
            gridInit = GridInit3D(isSpherePresent : true) as GridInit
        }
        
        print("1 - absorbing boundary condition, 0 - reflection")
        let boundaryType = intInput()

        if boundaryType == 0{
            abc =  emptyAbc() as AbsorbingBoundaryCondition
        }
        
        sourceFunction = Ricker2D() as SourceFunction
    }
    
    print("1 - additive source 0 - tfsf? ")
    let sourceInitiator = intInput()
    
    if sourceInitiator == 1{
        tfsf = emptytfsf() as TotalFieldScatteringField
        sourceFunction = additiveSourceFunction() as SourceFunction
    }


    return control(dimensions:dimensions, gridInit : gridInit, tfsf: tfsf, abc : abc, snapshot : snapshot, update : update, sourceFunction : sourceFunction)
}

public func runSimulation(){

    var ben = create_remote()
    ben.initialize()
    ben.iterate(maxTime : 450)
}

