
from grid import *


class UpdateFunction:
    
    def magneticField(g):return
    def electricField(g):return


class tmzUpdate(UpdateFunction) :


    def magneticField(g) :
        
        if (g.type == 1) :
            oneDUpdate().magneticField(g)
        
        
        else:

            for mm in range(0,g.size_x):
                for nn in range(0, g.size_y - 1):
                    hx[mm][nn] = chxh[mm][nn] * hx[mm][nn] - chxe[mm][nn] * (ez[mm][nn + 1] - ez[mm][nn])
                
            
            
            
            for mm in range(0, g.size_x - 1):
                for nn in range(0,g.size_y):
                    hy[mm][nn] = chyh[mm][nn] * hy[mm][nn] + chye[mm][nn] * (ez[mm + 1][nn] - ez[mm][nn])


    def electricField(g) :
        
        
        if (g.type == 1) :
            oneDUpdate().electricField(g)
        
        
        else:
            
            for mm in range(1, g.size_x - 1):
                for nn in range(1, g.size_y - 1):
                    ez[mm][nn] = ceze[mm][nn] * ez[mm][nn] + cezh[mm][nn] * (hy[mm][nn] - hy[mm - 1][nn]) - (hx[mm][nn] - hx[mm][nn - 1])
                
            
        
    

        
class tezUpdate(UpdateFunction) :

 
    def magneticField(g) :
        
        
        if(g.type == 1) :
            
            for mm in range( 0, g.size_x - 1):
                hz1[mm] = chzh1[mm] * hz1[mm] - chze1[mm] * (ey1[mm + 1] - ey1[mm])
            
        
            
        else :
            
            for mm in range( 0, g.size_x - 1):
                for nn in range( 0, g.size_y - 1):
                    hz[mm][nn] = chzh[mm][nn] * hz[mm][nn] + chze[mm][nn] * ((ex[mm][nn + 1] - ex[mm][nn])  - (ey[mm + 1][nn] - ey[mm][nn]))
                
            
        
        
    
    
    def electricField(g) :
        
        if(g.type == 1) :
            
            for mm in range(1, g.size_x - 1) :
                ey1[mm] = ceye1[mm] * ey1[mm] - ceyh1[mm] * (hz1[mm] - hz1[mm - 1])
            
        
            
        else :
        
            for mm in range(0, g.size_x - 1):
                for nn in range(1, g.size_y - 1):
                    ex[mm][nn] = cexe[mm][nn] * ex[mm][nn] + cexh[mm][nn] * (hz[mm][nn] - hz[mm][nn - 1])
                
            
                    
            for mm in range(1, g.size_x - 1):
                for nn in range(0, g.size_y - 1):
                    ey[mm][nn] = ceye[mm][nn] * ey[mm][nn] - ceyh[mm][nn] * (hz[mm][nn] - hz[mm - 1][nn])
                
            
            
        
    

    

class oneDUpdate(UpdateFunction):

    def magneticField(g) :
        
        for mm in range(0, g.size_x - 2) :
            hy1[mm] = chyh1[mm] * hy1[mm] +  chye1[mm] * (ez1[mm + 1] - ez1[mm])
        
        
    

    def electricField(g) :
        
        for mm in range(1, g.size_x - 2):
            ez1[mm] = ceze1[mm] * ez1[mm] +  cezh1[mm] * (hy1[mm] - hy1[mm - 1])
        
    



class update3D(UpdateFunction):
    
    def magneticField(g) :
        
        if (g.type == 1) :
            
            oneDUpdate().magneticField(g)
            
        elif (g.type == 2) :
            
            tmzUpdate().magneticField(g)
            
        elif (g.type == 3) :
            
            tezUpdate().magneticField(g)
        
        
        else:
        
            for mm in range(0, g.size_x - 1) :
                for nn in range(0,g.size_y - 1) :
                    for pp in range( 0,g.size_z - 1) :
                        hx3[mm][nn][pp] = chxh3[mm][nn][pp] * hx3[mm][nn][pp] +chxe3[mm][nn][pp] * ((ey3[mm][nn][pp + 1] - ey3[mm][nn][pp]) -(ez3[mm][nn + 1][pp] - ez3[mm][nn][pp]))
                    
                
            

            for mm in range( 0,g.size_x - 1):
                for nn in range( 0,g.size_y - 1) :
                    for pp in range( 0,g.size_z - 1) :
                        hy3[mm][nn][pp] = chyh3[mm][nn][pp] * hy3[mm][nn][pp] +  chye3[mm][nn][pp] * ((ez3[mm + 1][nn][pp] - ez3[mm][nn][pp]) -  (ex3[mm][nn][pp + 1] - ex3[mm][nn][pp]))
                    
                
            

            for mm in range( 0,g.size_x - 1) :
                for nn in range( 0,g.size_y - 1) :
                    for pp in range( 0,g.size_z):
                        hz3[mm][nn][pp] = chzh3[mm][nn][pp] * hz3[mm][nn][pp] +chze3[mm][nn][pp] * ((ex3[mm][nn + 1][pp] - ex3[mm][nn][pp]) -(ey3[mm + 1][nn][pp] - ey3[mm][nn][pp]))
                    
                
            
        
    
    
    def electricField(g) :
        
        if (g.type == 1) :
            
            oneDUpdate().electricField(g)
            
        elif (g.type == 2) :
            
            tmzUpdate().electricField(g)
            
        elif (g.type == 3) :
            
            tezUpdate().electricField(g)
            
        
        
        else:

            for mm in range( 0,g.size_x - 1) :
                for nn in range( 1,g.size_y - 1):
                    for pp in range( 1,g.size_z - 1):
                        ex3[mm][nn][pp] = cexe3[mm][nn][pp] * ex3[mm][nn][pp] +cexh3[mm][nn][pp] * ((hz3[mm][nn][pp] - hz3[mm][nn - 1][pp]) -(hy3[mm][nn][pp] - hy3[mm][nn][pp - 1]))
                    
                
            

            for mm in range( 1,g.size_x - 1):
                for nn in range( 0,g.size_y - 1):
                    for pp in range( 1,g.size_z - 1):
                        ey3[mm][nn][pp] = ceye3[mm][nn][pp] * ey3[mm][nn][pp] +ceyh3[mm][nn][pp] * ((hx3[mm][nn][pp] - hx3[mm][nn][pp - 1]) -(hz3[mm][nn][pp] - hz3[mm - 1][nn][pp]))
                    
                
            

            for mm in range( 1,g.size_x - 1):
                for nn in range( 1,g.size_y - 1):
                    for pp in range( 0,g.size_z - 1):
                        ez3[mm][nn][pp] = ceze3[mm][nn][pp] * ez3[mm][nn][pp] +cezh3[mm][nn][pp] * ((hy3[mm][nn][pp] - hy3[mm - 1][nn][pp]) -(hx3[mm][nn][pp] - hx3[mm][nn - 1][pp]))
                    
                
            
        
    

