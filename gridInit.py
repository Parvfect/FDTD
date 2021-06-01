

class GridInit:
    def initialize() 


class plain1DGridInit(GridInit):
    
    LOSS =  0.02
    LOSS_LAYER = 180 
    EPSR = 9.0
    
    def initialize()  :
        
        imp0 = 377.0
        size_x = 200   
        maxTime = 450 
        cdtds = 1.0  
        
        Ez = np.zeros(size_x)
        Ceze = np.zeros(size_x)
        Cezh = np.zeros(size_x)
        Hy = np.zeros(size_x-1)
        Chyh = np.zeros(size_x-1)
        Chye = np.zeros(size_x-1)
        
        for mm in range(size_x-1):
            
            if (mm < 100) :
                Ceze[mm] = 1.0
                Cezh[mm] = imp0
            
                
            else if (mm < LOSS_LAYER) :
                Ceze[mm] = 1.0
                Cezh[mm] = imp0 / EPSR
            
                
            else :
                Ceze[mm] = (1.0 - LOSS) / (1.0 + LOSS)
                Cezh[mm] = imp0 / EPSR / (1.0 + LOSS)
            
        
        
        for mm in range(size_x - 2) :
            
            if (mm < LOSS_LAYER) :
                Chyh[mm] = 1.0
                Chye[mm] = 1.0 / imp0
                
             else :
                Chyh[mm] = (1.0 - LOSS) / (1.0 + LOSS)
                Chye[mm] = 1.0 / imp0 / (1.0 + LOSS)
            
            
        
        
        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye
        
        return Grid(size_x:size_x, size_y: 0, size_z: 0,maxTime: maxTime, time:0, cdtds:cdtds, type: 1)
    


class auxillaryHzGridInit(GridInit):
    
    NLOSS = 20.0
    MAX_LOSS = 0.35
    
    def initialize() :
        
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        size_x = Int(NLOSS)
        MaxTime = 450
        
        Ey = np.zeros(size_x)
        Ceye = np.zeros(size_x)
        Ceyh = np.zeros(size_x)
        Hz = np.zeros(size_x-1)
        Chzh = np.zeros(size_x-1)
        Chze = np.zeros(size_x-1)
        
        for mm in range(size_x - 2):
            
            if (mm < size_x - 1 - Int(NLOSS)):
                Ceye[mm] = 1.0
                Ceyh[mm] = cdtds + imp0
                Chzh[mm] = 1.0
                Chze[mm] = cdtds / imp0
                
            
                
            else:
                depthInLayer += 0.5
                lossFactor = MAX_LOSS * pow(MAX_LOSS * 2.0, depthInLayer / Double(NLOSS))
                Ceye[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Ceyh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = MAX_LOSS  * pow(depthInLayer * 2.0, Double(NLOSS))
                Chzh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chze[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
        
        
        ey1 = Ey
        hz1 = Hz
        ceye1 = Ceye
        ceyh1 = Ceyh
        chzh1 = Chzh
        chze1 = Chze
        
        return Grid(size_x: size_x, size_y: 0, size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    

class auxillaryEzGridInit(GridInit):
    
    NLOSS = 20.0
    MAX_LOSS = 0.35
    
    def initialize() :
        
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        MaxTime = 450
        size_x = Int(NLOSS) 
        
        Ez = np.zeros(size_x)
        Ceze = np.zeros(size_x)
        Cezh = np.zeros(size_x)
        Hy = np.zeros(size_x-1)
        Chyh = np.zeros(size_x-1)
        Chye = np.zeros(size_x-1)
        
        for mm in range(size_x - 2):
            
            if (mm < size_x - 1 - Int(NLOSS)):
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            else:
                depthInLayer = Double((mm - size_x - 1 - Int(NLOSS))) + 0.5
                lossFactor = pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
            
        

        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye
        
        return Grid(size_x: size_x, size_y: 0 , size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    



class aux3DGridInit(GridInit):
    
    NLOSS = 25.0
    MAX_LOSS = 0.35
    
    def initialize() :
        
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        MaxTime = 450
        size_x = Int(NLOSS) 
        
        Ez = np.zeros(size_x)
        Ceze = np.zeros(size_x)
        Cezh = np.zeros(size_x)
        Hy = np.zeros(size_x-1)
        Chyh = np.zeros(size_x-1)
        Chye = np.zeros(size_x-1)
        
        for mm in range(size_x - 2) :
            
            if (mm < size_x - 1 - Int(NLOSS)):
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            
            else:
                depthInLayer += 0.5
                lossFactor = 0.35 * pow(depthInLayer / NLOSS, 2)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer += 0.5
                lossFactor = 0.35 * pow(depthInLayer / NLOSS, 2)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
            
        
        
        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye

        return Grid(size_x: size_x, size_y: 0 , size_z : 0, maxTime: MaxTime, time: 0, cdtds: cdtds, type : 1)
    


class tmzTfsfGridInit(GridInit):
    
    def initialize() :
        
        imp0 = 377.0
        size_x = 100            
        size_y = 81             
        maxTime = 10         
        cdtds = 1.0 / sqrt(2.0) 
        
        Ez = np.zeros((size_x, size_y))
        Ceze = np.zeros((size_x, size_y))
        Cezh = np.zeros((size_x, size_y))
        
        Hx = np.zeros((size_x, (size_y - 1)))
        Chxh = np.zeros((size_x, (size_y - 1))
        Chxe = np.zeros((size_x, (size_y - 1)))
        
        Hy = np.zeros((size_x - 1, size_y))
        Chyh = np.zeros(x:size_x - 1, y: size_y)
        Chye = np.zeros(x:size_x - 1, y: size_y)
        
        for mm in range(size_x :
            for nn in range(size_y:
                Ceze[mm][nn] = 1.0
                Cezh[mm][nn] = cdtds * imp0
            
        
        
        for mm in range(size_x:
            for nn in range(size_y - 1:
                Chxh[mm][nn] = 1.0
                Chxe[mm][nn] = cdtds / imp0
            
        
        
        for mm in range(size_x - 1:
            for nn in range(size_y:
                Chyh[mm][nn] = 1.0
                Chye[mm][nn] = cdtds / imp0
            
        
        
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
    


class tezGridInit(GridInit) :
    
    def initialize()  :
        
        imp0 = 377.0
        size_x = 92
        size_y = 82
        MaxTime = 10
        Cdtds = 1.0/sqrt(2.0)
        
        Ex = np.zeros(x: size_x - 1, y: size_y)
        Cexe = np.zeros(x: size_x - 1, y: size_y)
        Cexh = np.zeros(x: size_x - 1, y: size_y)
        
        Ey = np.zeros(x: size_x, y: size_y - 1)
        Ceye = np.zeros(x: size_x, y: size_y - 1)
        Ceyh = np.zeros(x: size_x, y: size_y - 1)
        
        Hz = np.zeros(x: size_x - 1, y: size_y - 1)
        Chzh = np.zeros(x: size_x - 1, y: size_y - 1)
        Chze = np.zeros(x: size_x - 1, y: size_y - 1)
        
        for mm in range(size_x-1):
            for nn in range(size_y):
                Cexe[mm][nn] = 1.0
                Cexh[mm][nn] = Cdtds * imp0
            
        
        
        for mm in range(size_x):
            for nn in range(size_y-1):
                Ceye[mm][nn] = 1.0
                Ceyh[mm][nn] = Cdtds * imp0
            
        
        
        rad = 12
        xCenter = size_x/2
        yCenter = size_y/2
        r2 = rad * rad
        
        xLocation = 0
        yLocation = 0
        
        for mm in 1...(size_x-1):
            xLocation = mm - xCenter
            
            for nn in 1...(size_y-1):
                yLocation = nn - yCenter
                if ((xLocation * xLocation + yLocation * yLocation) < r2):
                    Cexe[mm][nn] = 0.0
                    Cexh[mm][nn] = 0.0
                    Cexe[mm][nn + 1] = 0.0
                    Ceye[mm][nn + 1] = 0.0
                    Ceye[mm + 1][nn] = 0.0
                    Ceyh[mm + 1][nn] = 0.0
                    Ceye[mm][nn] = 0.0
                    Ceyh[mm][nn] = 0.0
                
            
        
        
        for mm in range(size_x-1):
            for nn in range(size_y-1):
                Chzh[mm][nn] = 1.0
                Chze[mm][nn] = Cdtds/imp0
            
        
        
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
    


class GridInit3D(GridInit):

    isSpherePresent : Bool
    
    def initialize()  :
        
        imp0 = 377.0
        type = 5
        size_x = 35
        size_y = 35
        size_z = 35
        Maxtime = 2
        cdtds = 1.0/sqrt(3.0)
        
        m_c = 17
        n_c = 17
        p_c = 17
        isSpherePresent:Bool
        m2:Double
        n2:Double
        p2:Double
        r2:Double
        rad = 8.0
        
        
        mm:Int = 0
        nn:Int = 0
        pp:Int = 0
        
        
        Ex = np.zeros(x: size_x - 1, y: size_y, z: size_z)
        Cexe = np.zeros(x: size_x - 1, y: size_y, z: size_z)
        Cexh = np.zeros(x: size_x - 1, y: size_y, z: size_z)
        
        Ey = np.zeros(x: size_x, y: size_y - 1, z: size_z)
        Ceye = np.zeros(x: size_x, y: size_y - 1, z: size_z)
        Ceyh = np.zeros(x: size_x, y: size_y - 1, z: size_z)
        
        Ez = np.zeros(x: size_x, y: size_y, z: size_z - 1)
        Ceze = np.zeros(x: size_x, y: size_y, z: size_z - 1)
        Cezh = np.zeros(x: size_x, y: size_y, z: size_z - 1)
        
        Hx = np.zeros(x: size_x, y: size_y - 1, z: size_z-1)
        Chxh = np.zeros(x: size_x, y: size_y - 1, z: size_z - 1)
        Chxe = np.zeros(x: size_x, y: size_y - 1, z: size_z - 1)
        
        Hy = np.zeros(x: size_x - 1, y: size_y, z: size_z-1)
        Chyh = np.zeros(x: size_x - 1, y: size_y, z: size_z-1)
        Chye = np.zeros(x: size_x - 1, y: size_y, z: size_z-1)
        
        Hz = np.zeros(x: size_x - 1, y: size_y - 1, z: size_z)
        Chzh = np.zeros(x: size_x - 1, y: size_y - 1, z: size_z)
        Chze = np.zeros(x: size_x - 1, y: size_y - 1, z: size_z)
        
        for mm in range(size_x - 1):
            for nn in range(size_y):
                for pp in range(size_z):
                    Cexe[mm][nn][pp] = 1.0
                    Cexh[mm][nn][pp] = cdtds * imp0
                
            
        
        
        for mm in range(size_x):
            for nn in range(size_y - 1):
                for pp in range(size_z):
                    Ceye[mm][nn][pp] = 1.0
                    Ceyh[mm][nn][pp] = cdtds / imp0
                
            
        
        
        for mm in range(size_x):
            for nn in range(size_y):
                for pp in range(size_z - 1):
                    Ceze[mm][nn][pp] = 1.0
                    Cezh[mm][nn][pp] = cdtds / imp0
                
            
        
        
        if self.isSpherePresent :
            r2 = rad * rad
            
            for mm in 2...(size_x - 2):
                m2 = (Double(mm) + 0.5 - Double(m_c)) * (Double(mm) + 0.5 - Double(n_c))
                
                for nn in 2...(size_y - 2):
                    n2 = (Double(nn) + 0.5 - Double(m_c)) * (Double(nn) + 0.5 - Double(n_c))
                    
                    for pp in 2...(size_z - 2):
                        p2 = (Double(pp) + 0.5 - Double(p_c)) * (Double(pp) + 0.5 - Double(p_c))
                        
                        if (m2+n2+p2<r2):
                            
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
                        
                    
                
            
        
        
        
        for mm in range(size_x):
            for nn in range(size_y - 1):
                for pp in range(size_z - 1):
                    Chxh[mm][nn][pp] = 1.0
                    Chxe[mm][nn][pp] = cdtds / imp0
                
            
        
        
        for mm in range(size_x - 1):
            for nn in range(size_y):
                for pp in range(size_z - 1):
                    Chyh[mm][nn][pp] = 1.0
                    Chye[mm][nn][pp] = cdtds / imp0
                
            
        
        
        for mm in range(size_x - 1):
            for nn in range(size_y - 1):
                for pp in range(size_z):
                    Chzh[mm][nn][pp] = 1.0
                    Chze[mm][nn][pp] = cdtds / imp0
                
            
        
        
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
    


