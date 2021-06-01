import numpy as np

ezLeft = np.zeros(g2.size_y * 6)
ezRight = np.zeros(g2.size_y * 6)
ezTop = np.zeros(g2.size_x * 6)
ezBottom = np.zeros(g2.size_x * 6)
eyLeft = np.zeros((g2.size_y - 1) * 6)
eyRight = np.zeros((g2.size_y - 1) * 6)
exTop = np.zeros((g2.size_x - 1) * 6)
exBottom = np.zeros((g2.size_x - 1) * 6)
ezOldLeft1 = np.zeros(3)
ezOldLeft2 = np.zeros(3)
ezOldRight1 = np.zeros(3)
ezOldRight2 = np.zeros(3)
AbcCoefLeft = np.zeros(3)
AbcCoefRight = np.zeros(3)


class AbsorbingBoundaryCondition:
    def initialize(g):
        pass

    def apply(g):
        pass



class emptyAbc(AbsorbingBoundaryCondition):
      def initialize(g):return
      def apply(g):return


 class plain1Dabc(AbsorbingBoundaryCondition):

    initdone = false

      def initialize(g):

        self.initdone = true
        temp1 = 0.0
        temp2 = 0.0
        
        temp1 = sqrt( cezh1[0] * chye1[0] )
        temp2 = 1.0 / temp1 + 2.0 + temp1
        AbcCoefLeft[0] = -(1.0 / temp1 - 2.0 + temp1) / temp2
        AbcCoefLeft[1] = -2.0 * (temp1 - 1.0 / temp1) / temp2
        AbcCoefLeft[2] = 4.0 * (temp1 + 1.0 / temp1) / temp2
        
        temp1 = sqrt(cezh1[g.size_x - 1] * chye1[g.size_x - 2])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        AbcCoefRight[0] = -(1.0 / temp1 - 2.0 + temp1) / temp2
        AbcCoefRight[1] = -2.0 * (temp1 - 1.0 / temp1) / temp2
        AbcCoefRight[2] = 4.0 * (temp1 + 1.0 / temp1) / temp2
        
    
    
      def apply(g):
        
        ez1[0] = AbcCoefLeft[0] * (ez1[2] + ezOldLeft1[0])
            + AbcCoefLeft[1] * (ezOldLeft1[0] + ezOldLeft1[2] -
                ez1[1] - ezOldLeft2[1])
        
        ez1[g.size_x - 1] =  AbcCoefRight[0] * (ez1[g.size_x - 3] + ezOldRight2[0])
            + AbcCoefRight[1] * (ezOldRight1[0] + ezOldRight1[2] -
                ez1[g.size_x - 2] - ezOldRight2[1])
            + AbcCoefRight[2] * ezOldRight1[1] - ezOldRight2[2]
        
        for mm in range2 :
            ezOldLeft2[mm] = ezOldLeft1[mm]
            ezOldLeft1[mm] = ez1[mm]
            ezOldRight2[mm] = ezOldRight1[mm]
            ezOldRight1[mm] = ez1[g.size_x - 1 - mm]
        
    




 class tezabc(AbsorbingBoundaryCondition):
   
    initDone = 0
    coef0 = 0.0
    coef1 = 0.0
    coef2 = 0.0
    
    
      def initialize(g: Grid):
        
        temp1 = 0.0
        temp2 = 0.0
    
        temp1  = sqrt(cexh[0][0] * chze[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    

      

      def apply(g :Grid):
    
        for nn in range(g.size_y - 1) :
            ey[0][nn] = coef0 * (ey[2][nn] + eyLeft[nqm(n:0, q:1, m:nn)]) + coef1 * (eyLeft[nqm(n:0, q:0, m:nn)] + eyLeft[nqm(n:2, q:0, m:nn)] - ey[1][nn] - eyLeft[nqm(n:1, q:1, m:nn)]) + coef2 * eyLeft[nqm(n:1, q:0, m:nn)] - eyLeft[nqm(n:2, q:1, m:nn)]

            for mm in range3 :
                eyLeft[nqm(n:mm, q:1, m:nn)] = eyLeft[nqm(n:mm, q:0, m:nn)]
                eyLeft[nqm(n:mm, q:0, m:nn)] = ey[mm][nn]
            
        
        
        for nn in range(g.size_y - 1) :
            ey[g.size_x - 1][nn] = coef0 * (ey[g.size_x - 3][nn] + eyRight[nqm(n:0, q:1, m:nn)]) + coef1 * (eyRight[nqm(n:0, q:0, m:nn)] + eyRight[nqm(n:2, q:0, m:nn)]) - ey[g.size_x - 2][nn] - eyRight[nqm(n:1, q:1, m:nn)] + coef2 * eyRight[nqm(n:1, q:0, m:nn)] - eyRight[nqm(n:2, q:1, m:nn)]
            
            for mm in range3 :
                eyRight[nqm(n:mm, q:1, m:nn)] = eyRight[nqm(n:mm, q:0, m:nn)]
                eyRight[nqm(n:mm, q:0, m:nn)] = ey[g.size_x - 1 - mm][nn]
            
        

        for mm in range(g.size_x - 1)  :
            ex[mm][0] = coef0 * (ex[mm][2] + exBottom[mqn(m:0, q:1, n:mm)]) + coef1 * (exBottom[mqn(m:0, q:0, n:mm)] + exBottom[mqn(m:2, q:0, n:mm)]  - ex[mm][1] - exBottom[mqn(m:1, q:1, n:mm)]) + coef2 * exBottom[mqn(m:1, q:0, n:mm)] - exBottom[mqn(m:2, q:1, n:mm)]
            
            for nn in range(3)  :
                exBottom[mqn(m:nn, q:1, n:mm)] = exBottom[mqn(m:nn, q:0, n:mm)]
                exBottom[mqn(m:nn, q:0, n:mm)] = ex[mm][nn]
            
        
        
        for mm in range(g.size_x - 1)  :
            ex[mm][g.size_y - 1] = coef0 * (ex[mm][g.size_y - 3] + exTop[mqn(m:0, q:1, n:mm)]) + coef1 * (exTop[mqn(m:0, q:0, n:mm)] + exTop[mqn(m:2, q:0, n:mm)] - ex[mm][g.size_y - 2] - exTop[mqn(m:1, q:1, n:mm)])    + coef2 * exTop[mqn(m:1, q:0, n:mm)] - exTop[mqn(m:2, q:1, n:mm)]
            
            for nn in range3  :
                exTop[mqn(m:nn, q:1, n:mm)] = exTop[mqn(m:nn, q:0, n:mm)]
                exTop[mqn(m:nn, q:0, n:mm)] = ex[mm][g.size_y - 1 - nn]
            
        
        
    

            
 class tmzabc(AbsorbingBoundaryCondition) :
    
    initDone = 0
    coef0 = 0.0
    coef1 = 0.0
    coef2 = 0.0
    
      def initialize(g: Grid):
        
        initDone = 1
        temp1 = 0.0
        temp2 = 0.0
        
        temp1 = sqrt(cezh[0][0] * chye[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    
    
      def apply(g: Grid):
    
        for nn in range(g.size_y):
            ez[0][nn] = coef0 * (ez[2][nn] + ezLeft[nqm(n:0, q:1, m:nn)]) + coef1 * (ezLeft[nqm(n:0, q:0, m:nn)] + ezLeft[nqm(n: 2, q:0, m:nn)] - ez[1][nn] - ezLeft[nqm(n:1, q:1, m:nn)]) + coef2 * ezLeft[nqm(n:1, q:0, m:nn)] - ezLeft[nqm(n:2, q:1, m:nn)]
        
            for mm in range(3) :
                ezLeft[nqm(n:mm, q:1, m:nn)] = ezLeft[nqm(n:mm, q:0, m:nn)]
                ezLeft[nqm(n:mm, q:0, m:nn)] = ez[mm][nn]
            
        
    
        for nn in range(g.size_y):
            ez[g.size_x - 1][nn] = coef0 * (ez[g.size_x - 3][nn] + ezRight[nqm(n:0, q:1, m:nn)]) + coef1 * (ezRight[nqm(n:0, q:0, m:nn)] + ezRight[nqm(n:2, q:0, m:nn)] - ez[g.size_x - 2][nn] - ezRight[nqm(n:1, q:1, m:nn)])  + coef2 * ezRight[nqm(n:1, q:0, m:nn)] - ezRight[nqm(n:2, q:1, m:nn)]
        
            for mm in range3 :
                ezRight[nqm(n:mm, q:1, m:nn)] = ezRight[nqm(n:mm, q:0, m:nn)]
                ezRight[nqm(n:mm, q:0, m:nn)] = ez[g.size_x - 1 - mm][nn]
            
        
    
        for mm in range(g.size_x):
            ez[mm][0] = coef0 * (ez[mm][2] + ezBottom[mqn(m:0, q:1, n:mm)]) + coef1 * (ezBottom[mqn(m:0, q:0, n:mm)] + ezBottom[mqn(m:2, q:0, n:mm)] - ez[mm][1] - ezBottom[mqn(m:1, q:1, n:mm)]) + coef2 * ezBottom[mqn(m:1, q:0, n:mm)] - ezBottom[mqn(m:2, q:1, n:mm)]
        
            for nn in range3:
                ezBottom[mqn(m:nn, q:1, n:mm)] = ezBottom[mqn(m:nn, q:0, n:mm)]
                ezBottom[mqn(m:nn, q:0, n:mm)] = ez[mm][nn]
            
        
        
        for mm in range(g.size_x) :
            ez[mm][g.size_y - 1] = coef0 * (ez[mm][g.size_y - 3] + ezTop[mqn(m:0, q:1, n:mm)])
            + coef1 * (ezTop[mqn(m:0, q:0, n:mm)] + ezTop[mqn(m:2, q:0, n:mm)]
            - ez[mm][g.size_y - 2] - ezTop[mqn(m:1, q:1, n:mm)])
            + coef2 * ezTop[mqn(m:1, q:0, n:mm)] - ezTop[mqn(m:2, q:1, n:mm)]
            
            for nn in range3:
                ezTop[mqn(m:nn, q:1, n:mm)] = ezTop[mqn(m:nn, q:0, n:mm)]
                ezTop[mqn(m:nn, q:0, n:mm)] = ez[mm][g.size_y - 1 - nn]
            
        
    



 class abc3d(AbsorbingBoundaryCondition):
            
        
    x = 0
    y = 0
    z = 0
    
    abccoef = 0.0
    
    exy0 = [[Double]]()
    exy1 = [[Double]]()
    exz0 = [[Double]]()
    exz1 = [[Double]]()
    eyx0 = [[Double]]()
    eyx1 = [[Double]]()
    eyz0 = [[Double]]()
    eyz1 = [[Double]]()
    ezx0 = [[Double]]()
    ezx1 = [[Double]]()
    ezy0 = [[Double]]()
    ezy1 = [[Double]]()
    
      def initialize(g: Grid) :
    
        cdtds = g.cdtds
        abccoef = (cdtds - 1.0) / (cdtds + 1.0)
        
        x = g.size_x
        y = g.size_y
        z = g.size_z
        
        eyx0 = make2DArray(x : g.size_y - 1, y : g.size_z)
        ezx0 = make2DArray(x : g.size_y, y : g.size_z - 1)
        eyx1 = make2DArray(x : g.size_y - 1, y : g.size_z)
        ezx1 = make2DArray(x : g.size_y, y : g.size_z - 1)
        
        exy0 = make2DArray(x : g.size_x - 1, y : g.size_z)
        ezy0 = make2DArray(x : g.size_x, y : g.size_z - 1)
        exy1 = make2DArray(x : g.size_x - 1, y : g.size_z)
        ezy1 = make2DArray(x : g.size_x, y : g.size_z - 1)
        
        exz0 = make2DArray(x : g.size_x - 1, y : g.size_y)
        eyz0 = make2DArray(x : g.size_x, y : g.size_y - 1)
        exz1 = make2DArray(x : g.size_x - 1, y : g.size_y)
        eyz1 = make2DArray(x : g.size_x, y : g.size_y - 1)
    
    
      def apply(g: Grid) :
        
        mm = 0, nn = 0, pp = 0
        
        mm = 0
        for nn in range(g.size_y - 1) :
            for pp in range(g.size_z):
                ey3[mm][nn][pp] = eyx0[nn][pp] +  abccoef * (ey3[mm + 1][nn][pp] - ey3[mm][nn][pp])
                eyx0[nn][pp] = ey3[mm + 1][nn][pp]
            
        
        
        for nn in range(g.size_y) :
            for pp in range(g.size_z- 1):
                ez3[mm][nn][pp] = ezx0[nn][pp] + abccoef * (ez3[mm + 1][nn][pp] - ez3[mm][nn][pp])
                ezx0[nn][pp] = ez3[mm + 1][nn][pp]
            
        
        
        mm = g.size_x - 1
        for nn in range(g.size_y - 1) :
            for pp in range(g.size_z):
                ey3[mm][nn][pp] = eyx1[nn][pp] + abccoef * (ey3[mm - 1][nn][pp] - ey3[mm][nn][pp])
                eyx1[nn][pp] = ey3[mm - 1][nn][pp]
            
        
            
        for nn in range(g.size_y) :
            for pp in range(g.size_z- 1):
                ez3[mm][nn][pp] = ezx1[nn][pp] + abccoef * (ez3[mm - 1][nn][pp] - ez3[mm][nn][pp])
                ezx1[nn][pp] = ez3[mm - 1][nn][pp]
            
        
            
        nn = 0
        for mm in range(g.size_x - 1) :
            for pp in range(g.size_z):
                ex3[mm][nn][pp] = exy0[mm][pp] + abccoef * (ex3[mm][nn + 1][pp] - ex3[mm][nn][pp])
                exy0[mm][pp] = ex3[mm][nn + 1][pp]
            
        
        
        for mm in range(g.size_x) :
            for pp in range(g.size_z- 1):
                ez3[mm][nn][pp] = ezy0[mm][pp] + abccoef * (ez3[mm][nn + 1][pp] - ez3[mm][nn][pp])
                ezy0[mm][pp] = ez3[mm][nn + 1][pp]
            
        
        
        nn = g.size_y - 1
        for mm in range(g.size_x - 1) :
            for pp in range(g.size_z):
                ex3[mm][nn][pp] = exy1[mm][pp] + abccoef * (ex3[mm][nn - 1][pp] - ex3[mm][nn][pp])
                exy1[mm][pp] = ex3[mm][nn - 1][pp]
            
        
            
        for mm in range(g.size_x) :
            for pp in range(g.size_z)- 1):
                ez3[mm][nn][pp] = ezy1[mm][pp] + abccoef * (ez3[mm][nn - 1][pp] - ez3[mm][nn][pp])
                ezy1[mm][pp] = ez3[mm][nn - 1][pp]
            
        
        
        pp = 0
        for mm in range(g.size_x - 1) :
            for nn in range(g.size_y) :
                ex3[mm][nn][pp] = exz0[mm][nn] + abccoef * (ex3[mm][nn][pp + 1] - ex3[mm][nn][pp])
                exz0[mm][nn] = ex3[mm][nn][pp + 1]
            
        
            
        for mm in range(g.size_x) :
            for nn in range(g.size_y - 1) :
                ey3[mm][nn][pp] = eyz0[mm][nn] + abccoef * (ey3[mm][nn][pp + 1] - ey3[mm][nn][pp])
                eyz0[mm][nn] = ey3[mm][nn][pp + 1]
            
        
            
        pp = g.size_z - 1
        for mm in range(g.size_x - 1) :
            for nn in range(g.size_y) :
                ex3[mm][nn][pp] = exz1[mm][nn] + abccoef * (ex3[mm][nn][pp - 1] - ex3[mm][nn][pp])
                exz1[mm][nn] = ex3[mm][nn][pp - 1]
            
        
            
        for mm in range(g.size_x) :
            for nn in range(g.size_y - 1) :
                ey3[mm][nn][pp] = eyz1[mm][nn] + abccoef * (ey3[mm][nn][pp - 1] - ey3[mm][nn][pp])
                eyz1[mm][nn] = ey3[mm][nn][pp - 1]
            
        
    

                
                





