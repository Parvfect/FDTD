from grid import *
import numpy as np
import math

class GridInit:
    def initialize(self):
        pass


class plain1DGridInit(GridInit):
    
    
    def initialize(self):
        
        LOSS =  0.02
        LOSS_LAYER = 180 
        EPSR = 9.0

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
            
                
            elif (mm < LOSS_LAYER) :
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
        
        return Grid(size_x,  0,  0, maxTime, 0, cdtds,  1)
    


class auxillaryHzGridInit(GridInit):
    
    def initialize(self) :
            
        NLOSS = 20.0
        MAX_LOSS = 0.35
        
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        size_x = int(NLOSS)
        MaxTime = 450
        
        Ey = np.zeros(size_x)
        Ceye = np.zeros(size_x)
        Ceyh = np.zeros(size_x)
        Hz = np.zeros(size_x-1)
        Chzh = np.zeros(size_x-1)
        Chze = np.zeros(size_x-1)
        
        for mm in range(size_x - 2):
            
            if (mm < size_x - 1 - int(NLOSS)):
                Ceye[mm] = 1.0
                Ceyh[mm] = cdtds + imp0
                Chzh[mm] = 1.0
                Chze[mm] = cdtds / imp0
                
            
                
            else:
                depthInLayer = depthInLayer + 0.5
                lossFactor = MAX_LOSS * math.pow(MAX_LOSS * 2.0, depthInLayer / float(NLOSS))
                Ceye[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Ceyh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer = depthInLayer + 0.5
                lossFactor = MAX_LOSS  * math.pow(depthInLayer * 2.0, float(NLOSS))
                Chzh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chze[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
        
        
        ey1 = Ey
        hz1 = Hz
        ceye1 = Ceye
        ceyh1 = Ceyh
        chzh1 = Chzh
        chze1 = Chze
        
        return Grid( size_x,  0,  0,  MaxTime,  0,  cdtds,  1)
    

class auxillaryEzGridInit(GridInit):
    
    
    def initialize(self) :
        
        NLOSS = 20.0
        MAX_LOSS = 0.35
    
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        MaxTime = 450
        size_x = int(NLOSS) 
        
        Ez = np.zeros(size_x)
        Ceze = np.zeros(size_x)
        Cezh = np.zeros(size_x)
        Hy = np.zeros(size_x-1)
        Chyh = np.zeros(size_x-1)
        Chye = np.zeros(size_x-1)
        
        for mm in range(size_x - 2):
            
            if (mm < size_x - 1 - int(NLOSS)):
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            else:
                depthInLayer = float((mm - size_x - 1 - int(NLOSS))) + 0.5
                lossFactor = math.pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer = depthInLayer +0.5
                lossFactor = math.pow(MAX_LOSS * 2.0, depthInLayer / NLOSS)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
            
        

        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye
        
        return Grid( size_x, 0 ,  0, MaxTime,  0,  cdtds,  1)
    



class aux3DGridInit(GridInit):
    
   
    
    def initialize(self) :

        NLOSS = 25.0
        MAX_LOSS = 0.35 
        imp0 = 377.0
        depthInLayer = 0.0
        lossFactor = 0.0
        cdtds = 1.0
        MaxTime = 450
        size_x = int(NLOSS) 
        
        Ez = np.zeros(size_x)
        Ceze = np.zeros(size_x)
        Cezh = np.zeros(size_x)
        Hy = np.zeros(size_x-1)
        Chyh = np.zeros(size_x-1)
        Chye = np.zeros(size_x-1)
        
        for mm in range(size_x - 2) :
            
            if (mm < size_x - 1 - int(NLOSS)):
                Ceze[mm] = 1.0
                Cezh[mm] = cdtds * imp0
                Chyh[mm] = 1.0
                Chye[mm] = cdtds/imp0
            
            else:
                depthInLayer = depthInLayer +0.5
                lossFactor = 0.35 * math.pow(depthInLayer / NLOSS, 2)
                Ceze[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Cezh[mm] = cdtds * imp0 / (1.0 + lossFactor)
                depthInLayer = depthInLayer +0.5
                lossFactor = 0.35 * math.pow(depthInLayer / NLOSS, 2)
                Chyh[mm] = (1.0 - lossFactor) / (1.0 + lossFactor)
                Chye[mm] = cdtds / imp0 / (1.0 + lossFactor)
            
            
        
        
        ez1 = Ez
        hy1 = Hy
        ceze1 = Ceze
        cezh1 = Cezh
        chyh1 = Chyh
        chye1 = Chye

        return Grid( size_x,  0 ,  0, MaxTime,  0,  cdtds,  1)
    


class tmzTfsfGridInit(GridInit):
    
    def initialize(self) :
        
        imp0 = 377.0
        size_x = 100            
        size_y = 81             
        maxTime = 10         
        cdtds = 1.0 / sqrt(2.0) 
        
        Ez = np.zeros((size_x, size_y))
        Ceze = np.zeros((size_x, size_y))
        Cezh = np.zeros((size_x, size_y))
        
        Hx = np.zeros((size_x, (size_y - 1)))
        Chxh = np.zeros((size_x, (size_y - 1)))
        Chxe = np.zeros((size_x, (size_y - 1)))
        
        Hy = np.zeros((size_x - 1, size_y))
        Chyh = np.zeros((size_x - 1, size_y))
        Chye = np.zeros((size_x - 1, size_y))
        
        for mm in range(size_x) :
            for nn in range(size_y):
                Ceze[mm][nn] = 1.0
                Cezh[mm][nn] = cdtds * imp0
            
        
        
        for mm in range(size_x):
            for nn in range(size_y - 1):
                Chxh[mm][nn] = 1.0
                Chxe[mm][nn] = cdtds / imp0
            
        
        
        for mm in range(size_x - 1):
            for nn in range(size_y):
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
        
        return Grid(size_x, size_y,  0,  maxTime,  0,  cdtds,  2)
    


class tezGridInit(GridInit) :
    
    def initialize(self)  :
        
        imp0 = 377.0
        size_x = 92
        size_y = 82
        MaxTime = 10
        Cdtds = 1.0/sqrt(2.0)
        
        Ex = np.zeros(size_x - 1, size_y)
        Cexe = np.zeros(size_x - 1, size_y)
        Cexh = np.zeros(size_x - 1, size_y)
        
        Ey = np.zeros(size_x, size_y - 1)
        Ceye = np.zeros(size_x, size_y - 1)
        Ceyh = np.zeros(size_x, size_y - 1)
        
        Hz = np.zeros(size_x - 1, size_y - 1)
        Chzh = np.zeros(size_x - 1, size_y - 1)
        Chze = np.zeros(size_x - 1, size_y - 1)
        
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
        
        for mm in range(1,size_x-1):
            xLocation = mm - xCenter
            
            for nn in range(1,size_y-1):
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
        
        return Grid(size_x, size_y,  0, MaxTime,  0,  Cdtds,  3)
    


class GridInit3D(GridInit):

    
    def initialize(self, isSpherePresent)  :
        
        imp0 = 377.0
        Type = 5
        size_x = 35
        size_y = 35
        size_z = 35
        Maxtime = 2
        cdtds = 1.0/sqrt(3.0)
        
        m_c = 17
        n_c = 17
        p_c = 17
        rad = 8.0
        
        
        mm:int = 0
        nn:int = 0
        pp:int = 0
        
        
        Ex = np.zeros((size_x - 1, size_y, size_z))
        Cexe = np.zeros((size_x - 1, size_y, size_z))
        Cexh = np.zeros((size_x - 1, size_y, size_z))
        
        Ey = np.zeros((size_x, size_y - 1, size_z))
        Ceye = np.zeros((size_x, size_y - 1, size_z))
        Ceyh = np.zeros((size_x, size_y - 1, size_z))
        
        Ez = np.zeros((size_x, size_y, size_z - 1))
        Ceze = np.zeros((size_x, size_y, size_z - 1))
        Cezh = np.zeros((size_x, size_y, size_z - 1))
        
        Hx = np.zeros((size_x, size_y - 1, size_z-1))
        Chxh = np.zeros((size_x, size_y - 1, size_z-1))
        Chxe = np.zeros((size_x, size_y - 1, size_z-1))
        
        Hy = np.zeros((size_x - 1, size_y, size_z-1))
        Chyh = np.zeros((size_x - 1, size_y, size_z-1))
        Chye = np.zeros((size_x - 1, size_y, size_z-1))
        
        Hz = np.zeros((size_x - 1, size_y - 1, size_z))
        Chzh = np.zeros((size_x - 1, size_y - 1, size_z))
        Chze = np.zeros((size_x - 1, size_y - 1, size_z))
        
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
                
            
        
        
        if isSpherePresent :
            r2 = rad * rad
            
            for mm in range(2,size_x - 2):
                m2 = (float(mm) + 0.5 - float(m_c)) * (float(mm) + 0.5 - float(n_c))
                
                for nn in range(2,size_y - 2):
                    n2 = (float(nn) + 0.5 - float(m_c)) * (float(nn) + 0.5 - float(n_c))
                    
                    for pp in range(2,size_z - 2):
                        p2 = (float(pp) + 0.5 - float(p_c)) * (float(pp) + 0.5 - float(p_c))
                        
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
        
        return Grid(size_x, size_y, size_z, Maxtime,0, cdtds, 4)
    


