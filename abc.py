import numpy as np
from grid import *
from useful_functions import *
from control import *

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
eyx0 = np.zeros((g.size_y - 1, g.size_z))
ezx0 = np.zeros((g.size_y, g.size_z - 1))
eyx1 = np.zeros((g.size_y - 1, g.size_z))
ezx1 = np.zeros((g.size_y, g.size_z - 1))

exy0 = np.zeros((g.size_x - 1, g.size_z))
ezy0 = np.zeros((g.size_x, g.size_z - 1))
exy1 = np.zeros((g.size_x - 1, g.size_z))
ezy1 = np.zeros((g.size_x, g.size_z - 1))

exz0 = np.zeros((g.size_x - 1, g.size_y))
eyz0 = np.zeros((g.size_x, g.size_y - 1))
exz1 = np.zeros((g.size_x - 1, g.size_y))
eyz1 = np.zeros((g.size_x, g.size_y - 1))
    

class AbsorbingBoundaryCondition:
    def initialize(self, g):
        pass

    def apply(self, g):
        pass



class emptyAbc(AbsorbingBoundaryCondition):
      def initialize(self, g):return
      def apply(self, g):return


class plain1Dabc(AbsorbingBoundaryCondition):

    def initialize(self, g):

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
        


    def apply(self, g):
        
        ez1[0] = AbcCoefLeft[0] * (ez1[2] + ezOldLeft1[0])
        + AbcCoefLeft[1] * (ezOldLeft1[0] + ezOldLeft1[2] -
        ez1[1] - ezOldLeft2[1])
        
        ez1[g.size_x - 1] =  AbcCoefRight[0] * (ez1[g.size_x - 3] + ezOldRight2[0])
        + AbcCoefRight[1] * (ezOldRight1[0] + ezOldRight1[2] -
        ez1[g.size_x - 2] - ezOldRight2[1])
        + AbcCoefRight[2] * ezOldRight1[1] - ezOldRight2[2]
        
        for mm in range(2) :
            ezOldLeft2[mm] = ezOldLeft1[mm]
            ezOldLeft1[mm] = ez1[mm]
            ezOldRight2[mm] = ezOldRight1[mm]
            ezOldRight1[mm] = ez1[g.size_x - 1 - mm]
        





class tezabc(AbsorbingBoundaryCondition):
    
    def initialize(self, g):
        
        temp1 = 0.0
        temp2 = 0.0
    
        temp1  = sqrt(cexh[0][0] * chze[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    

      

    def apply(self, g):
    
        for nn in range(g.size_y - 1) :
            ey[0][nn] = coef0 * (ey[2][nn] + eyLeft[nqm(0, 1, nn)]) + coef1 * (eyLeft[nqm(0, 0, nn)] + eyLeft[nqm(2, 0, nn)] - ey[1][nn] - eyLeft[nqm(1, 1, nn)]) + coef2 * eyLeft[nqm(1, 0, nn)] - eyLeft[nqm(2, 1, nn)]

            for mm in range3 :
                eyLeft[nqm(mm, 1, nn)] = eyLeft[nqm(mm, 0, nn)]
                eyLeft[nqm(mm, 0, nn)] = ey[mm][nn]
            
        
        
        for nn in range(g.size_y - 1) :
            ey[g.size_x - 1][nn] = coef0 * (ey[g.size_x - 3][nn] + eyRight[nqm(0, 1, nn)]) + coef1 * (eyRight[nqm(0, 0, nn)] + eyRight[nqm(2, 0, nn)]) - ey[g.size_x - 2][nn] - eyRight[nqm(1, 1, nn)] + coef2 * eyRight[nqm(1, 0, nn)] - eyRight[nqm(2, 1, nn)]
            
            for mm in range3 :
                eyRight[nqm(mm, 1, nn)] = eyRight[nqm(mm, 0, nn)]
                eyRight[nqm(mm, 0, nn)] = ey[g.size_x - 1 - mm][nn]
            
        

        for mm in range(g.size_x - 1)  :
            ex[mm][0] = coef0 * (ex[mm][2] + exBottom[mqn(0, 1, mm)]) + coef1 * (exBottom[mqn(0, 0, mm)] + exBottom[mqn(2, 0, mm)]  - ex[mm][1] - exBottom[mqn(1, 1, mm)]) + coef2 * exBottom[mqn(1, 0, mm)] - exBottom[mqn(2, 1, mm)]
            
            for nn in range(3)  :
                exBottom[mqn(nn, 1, mm)] = exBottom[mqn(nn, 0, mm)]
                exBottom[mqn(nn, 0, mm)] = ex[mm][nn]
            
        
        
        for mm in range(g.size_x - 1)  :
            ex[mm][g.size_y - 1] = coef0 * (ex[mm][g.size_y - 3] + exTop[mqn(0, 1, mm)]) + coef1 * (exTop[mqn(0, 0, mm)] + exTop[mqn(2, 0, mm)] - ex[mm][g.size_y - 2] - exTop[mqn(1, 1, mm)])    + coef2 * exTop[mqn(1, 0, mm)] - exTop[mqn(2, 1, mm)]
            
            for nn in range(3)  :
                exTop[mqn(nn, 1, mm)] = exTop[mqn(nn, 0, mm)]
                exTop[mqn(nn, 0, mm)] = ex[mm][g.size_y - 1 - nn]
            
        
        
    

            
class tmzabc(AbsorbingBoundaryCondition) :

    def initialize(self, g):
        
        initDone = 1
        temp1 = 0.0
        temp2 = 0.0
        
        temp1 = sqrt(cezh[0][0] * chye[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    
    
    def apply(self, g):
    
        for nn in range(g.size_y):
            ez[0][nn] = coef0 * (ez[2][nn] + ezLeft[nqm(0, 1, nn)]) + coef1 * (ezLeft[nqm(0, 0, nn)] + ezLeft[nqm( 2, 0, nn)] - ez[1][nn] - ezLeft[nqm(1, 1, nn)]) + coef2 * ezLeft[nqm(1, 0, nn)] - ezLeft[nqm(2, 1, nn)]
        
            for mm in range(3) :
                ezLeft[nqm(mm, 1, nn)] = ezLeft[nqm(mm, 0, nn)]
                ezLeft[nqm(mm, 0, nn)] = ez[mm][nn]
            
        
    
        for nn in range(g.size_y):
            ez[g.size_x - 1][nn] = coef0 * (ez[g.size_x - 3][nn] + ezRight[nqm(0, 1, nn)]) + coef1 * (ezRight[nqm(0, 0, nn)] + ezRight[nqm(2, 0, nn)] - ez[g.size_x - 2][nn] - ezRight[nqm(1, 1, nn)])  + coef2 * ezRight[nqm(1, 0, nn)] - ezRight[nqm(2, 1, nn)]
        
            for mm in range3 :
                ezRight[nqm(mm, 1, nn)] = ezRight[nqm(mm, 0, nn)]
                ezRight[nqm(mm, 0, nn)] = ez[g.size_x - 1 - mm][nn]
            
        
    
        for mm in range(g.size_x):
            ez[mm][0] = coef0 * (ez[mm][2] + ezBottom[mqn(0, 1, mm)]) + coef1 * (ezBottom[mqn(0, 0, mm)] + ezBottom[mqn(2, 0, mm)] - ez[mm][1] - ezBottom[mqn(1, 1, mm)]) + coef2 * ezBottom[mqn(1, 0, mm)] - ezBottom[mqn(2, 1, mm)]
        
            for nn in range(3):
                ezBottom[mqn(nn, 1, mm)] = ezBottom[mqn(nn, 0, mm)]
                ezBottom[mqn(nn, 0, mm)] = ez[mm][nn]
            
        
        
        for mm in range(g.size_x) :
            ez[mm][g.size_y - 1] = coef0 * (ez[mm][g.size_y - 3] + ezTop[mqn(0, 1, mm)])
            + coef1 * (ezTop[mqn(0, 0, mm)] + ezTop[mqn(2, 0, mm)]
            - ez[mm][g.size_y - 2] - ezTop[mqn(1, 1, mm)])
            + coef2 * ezTop[mqn(1, 0, mm)] - ezTop[mqn(2, 1, mm)]
            
            for nn in range(3):
                ezTop[mqn(nn, 1, mm)] = ezTop[mqn(nn, 0, mm)]
                ezTop[mqn(nn, 0, mm)] = ez[mm][g.size_y - 1 - nn]
            
        
    



class abc3d(AbsorbingBoundaryCondition):
            
    def initialize(self, g) :
    
        cdtds = g.cdtds
        abccoef = (cdtds - 1.0) / (cdtds + 1.0)
        
        x = g.size_x
        y = g.size_y
        z = g.size_z
        
       
    
    def apply(self, g) :
        
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
            for pp in range(g.size_z- 1):
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
            
        
    

                
                





