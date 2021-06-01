import Foundation

var ezLeft = make1DArray(size : g2.size_y * 6)
var ezRight = make1DArray(size : g2.size_y * 6)
var ezTop = make1DArray(size : g2.size_x * 6)
var ezBottom = make1DArray(size : g2.size_x * 6)
var eyLeft = make1DArray(size : ((g2.size_y - 1) * 6))
var eyRight = make1DArray(size : ((g2.size_y - 1) * 6))
var exTop = make1DArray(size : ((g2.size_x - 1) * 6))
var exBottom = make1DArray(size : ((g2.size_x - 1) * 6))
var ezOldLeft1:[Double] = make1DArray(size : 3)
var ezOldLeft2:[Double] = make1DArray(size : 3)
var ezOldRight1:[Double] = make1DArray(size : 3)
var ezOldRight2:[Double] = make1DArray(size : 3)
var AbcCoefLeft:[Double] = make1DArray(size : 3)
var AbcCoefRight:[Double] = make1DArray(size : 3)


public protocol AbsorbingBoundaryCondition{
    mutating func initialize(g : Grid)
    mutating func apply(g : Grid)
}


public struct emptyAbc : AbsorbingBoundaryCondition{
    public mutating func initialize(g : Grid){return}
    public mutating func apply(g : Grid){return}
}

public struct plain1Dabc : AbsorbingBoundaryCondition{

    var initdone = false

    public mutating func initialize(g : Grid){

        self.initdone = true
        var temp1 = 0.0
        var temp2 = 0.0
        
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
        
    }
    
    public mutating func apply(g : Grid){
        
        ez1[0] = AbcCoefLeft[0] * (ez1[2] + ezOldLeft1[0])
            + AbcCoefLeft[1] * (ezOldLeft1[0] + ezOldLeft1[2] -
                ez1[1] - ezOldLeft2[1])
        
        ez1[g.size_x - 1] =  AbcCoefRight[0] * (ez1[g.size_x - 3] + ezOldRight2[0])
            + AbcCoefRight[1] * (ezOldRight1[0] + ezOldRight1[2] -
                ez1[g.size_x - 2] - ezOldRight2[1])
            + AbcCoefRight[2] * ezOldRight1[1] - ezOldRight2[2]
        
        for mm in 0...2 {
            ezOldLeft2[mm] = ezOldLeft1[mm]
            ezOldLeft1[mm] = ez1[mm]
            ezOldRight2[mm] = ezOldRight1[mm]
            ezOldRight1[mm] = ez1[g.size_x - 1 - mm]
        }
    }
}



public struct tezabc: AbsorbingBoundaryCondition{
   
    var initDone = 0
    var coef0 = 0.0
    var coef1 = 0.0
    var coef2 = 0.0
    
    
    public mutating func initialize(g: Grid){
        
        var temp1 = 0.0
        var temp2 = 0.0
    
        temp1  = sqrt(cexh[0][0] * chze[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    }

      

    public mutating func apply(g :Grid){
    
        for nn in 0...(g.size_y - 1) {
            ey[0][nn] = coef0 * (ey[2][nn] + eyLeft[nqm(n:0, q:1, m:nn)]) + coef1 * (eyLeft[nqm(n:0, q:0, m:nn)] + eyLeft[nqm(n:2, q:0, m:nn)] - ey[1][nn] - eyLeft[nqm(n:1, q:1, m:nn)]) + coef2 * eyLeft[nqm(n:1, q:0, m:nn)] - eyLeft[nqm(n:2, q:1, m:nn)]

            for mm in 0...3 {
                eyLeft[nqm(n:mm, q:1, m:nn)] = eyLeft[nqm(n:mm, q:0, m:nn)]
                eyLeft[nqm(n:mm, q:0, m:nn)] = ey[mm][nn]
            }
        }
        
        for nn in 0...(g.size_y - 1) {
            ey[g.size_x - 1][nn] = coef0 * (ey[g.size_x - 3][nn] + eyRight[nqm(n:0, q:1, m:nn)]) + coef1 * (eyRight[nqm(n:0, q:0, m:nn)] + eyRight[nqm(n:2, q:0, m:nn)]) - ey[g.size_x - 2][nn] - eyRight[nqm(n:1, q:1, m:nn)] + coef2 * eyRight[nqm(n:1, q:0, m:nn)] - eyRight[nqm(n:2, q:1, m:nn)]
            
            for mm in 0...3 {
                eyRight[nqm(n:mm, q:1, m:nn)] = eyRight[nqm(n:mm, q:0, m:nn)]
                eyRight[nqm(n:mm, q:0, m:nn)] = ey[g.size_x - 1 - mm][nn]
            }
        }

        for mm in 0...(g.size_x - 1)  {
            ex[mm][0] = coef0 * (ex[mm][2] + exBottom[mqn(m:0, q:1, n:mm)]) + coef1 * (exBottom[mqn(m:0, q:0, n:mm)] + exBottom[mqn(m:2, q:0, n:mm)]  - ex[mm][1] - exBottom[mqn(m:1, q:1, n:mm)]) + coef2 * exBottom[mqn(m:1, q:0, n:mm)] - exBottom[mqn(m:2, q:1, n:mm)]
            
            for nn in 0...3  {
                exBottom[mqn(m:nn, q:1, n:mm)] = exBottom[mqn(m:nn, q:0, n:mm)]
                exBottom[mqn(m:nn, q:0, n:mm)] = ex[mm][nn]
            }
        }
        
        for mm in 0...(g.size_x - 1)  {
            ex[mm][g.size_y - 1] = coef0 * (ex[mm][g.size_y - 3] + exTop[mqn(m:0, q:1, n:mm)]) + coef1 * (exTop[mqn(m:0, q:0, n:mm)] + exTop[mqn(m:2, q:0, n:mm)] - ex[mm][g.size_y - 2] - exTop[mqn(m:1, q:1, n:mm)])    + coef2 * exTop[mqn(m:1, q:0, n:mm)] - exTop[mqn(m:2, q:1, n:mm)]
            
            for nn in 0...3  {
                exTop[mqn(m:nn, q:1, n:mm)] = exTop[mqn(m:nn, q:0, n:mm)]
                exTop[mqn(m:nn, q:0, n:mm)] = ex[mm][g.size_y - 1 - nn]
            }
        }
        
    }
}
            
public struct tmzabc: AbsorbingBoundaryCondition {
    
    var initDone = 0
    var coef0 = 0.0
    var coef1 = 0.0
    var coef2 = 0.0
    
    public mutating func initialize(g: Grid){
        
        var initDone = 1
        var temp1 = 0.0
        var temp2 = 0.0
        
        temp1 = sqrt(cezh[0][0] * chye[0][0])
        temp2 = 1.0 / temp1 + 2.0 + temp1
        coef0 = -(1.0 / temp1 - 2.0 + temp1) / temp2
        coef1 = -2.0 * (temp1 - 1.0 / temp1) / temp2
        coef2 = 4.0 * (temp1 + 1.0 / temp1) / temp2
    }
    
    public mutating func apply(g: Grid){
    
        for nn in 0...g.size_y{
            ez[0][nn] = coef0 * (ez[2][nn] + ezLeft[nqm(n:0, q:1, m:nn)]) + coef1 * (ezLeft[nqm(n:0, q:0, m:nn)] + ezLeft[nqm(n: 2, q:0, m:nn)] - ez[1][nn] - ezLeft[nqm(n:1, q:1, m:nn)]) + coef2 * ezLeft[nqm(n:1, q:0, m:nn)] - ezLeft[nqm(n:2, q:1, m:nn)]
        
            for mm in 0...3 {
                ezLeft[nqm(n:mm, q:1, m:nn)] = ezLeft[nqm(n:mm, q:0, m:nn)]
                ezLeft[nqm(n:mm, q:0, m:nn)] = ez[mm][nn]
            }
        }
    
        for nn in 0...g.size_y{
            ez[g.size_x - 1][nn] = coef0 * (ez[g.size_x - 3][nn] + ezRight[nqm(n:0, q:1, m:nn)]) + coef1 * (ezRight[nqm(n:0, q:0, m:nn)] + ezRight[nqm(n:2, q:0, m:nn)] - ez[g.size_x - 2][nn] - ezRight[nqm(n:1, q:1, m:nn)])  + coef2 * ezRight[nqm(n:1, q:0, m:nn)] - ezRight[nqm(n:2, q:1, m:nn)]
        
            for mm in 0...3 {
                ezRight[nqm(n:mm, q:1, m:nn)] = ezRight[nqm(n:mm, q:0, m:nn)]
                ezRight[nqm(n:mm, q:0, m:nn)] = ez[g.size_x - 1 - mm][nn]
            }
        }
    
        for mm in 0...g.size_x {
            ez[mm][0] = coef0 * (ez[mm][2] + ezBottom[mqn(m:0, q:1, n:mm)]) + coef1 * (ezBottom[mqn(m:0, q:0, n:mm)] + ezBottom[mqn(m:2, q:0, n:mm)] - ez[mm][1] - ezBottom[mqn(m:1, q:1, n:mm)]) + coef2 * ezBottom[mqn(m:1, q:0, n:mm)] - ezBottom[mqn(m:2, q:1, n:mm)]
        
            for nn in 0...3{
                ezBottom[mqn(m:nn, q:1, n:mm)] = ezBottom[mqn(m:nn, q:0, n:mm)]
                ezBottom[mqn(m:nn, q:0, n:mm)] = ez[mm][nn]
            }
        }
        
        for mm in 0...g.size_x {
            ez[mm][g.size_y - 1] = coef0 * (ez[mm][g.size_y - 3] + ezTop[mqn(m:0, q:1, n:mm)])
            + coef1 * (ezTop[mqn(m:0, q:0, n:mm)] + ezTop[mqn(m:2, q:0, n:mm)]
            - ez[mm][g.size_y - 2] - ezTop[mqn(m:1, q:1, n:mm)])
            + coef2 * ezTop[mqn(m:1, q:0, n:mm)] - ezTop[mqn(m:2, q:1, n:mm)]
            
            for nn in 0...3{
                ezTop[mqn(m:nn, q:1, n:mm)] = ezTop[mqn(m:nn, q:0, n:mm)]
                ezTop[mqn(m:nn, q:0, n:mm)] = ez[mm][g.size_y - 1 - nn]
            }
        }
    }
}


public struct abc3d: AbsorbingBoundaryCondition{
            
        
    var x = 0
    var y = 0
    var z = 0
    
    var abccoef = 0.0
    
    var exy0 = [[Double]]()
    var exy1 = [[Double]]()
    var exz0 = [[Double]]()
    var exz1 = [[Double]]()
    var eyx0 = [[Double]]()
    var eyx1 = [[Double]]()
    var eyz0 = [[Double]]()
    var eyz1 = [[Double]]()
    var ezx0 = [[Double]]()
    var ezx1 = [[Double]]()
    var ezy0 = [[Double]]()
    var ezy1 = [[Double]]()
    
    public mutating func initialize(g: Grid) {
    
        var cdtds = g.cdtds
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
    }
    
    public mutating func apply(g: Grid) {
        
        var mm = 0, nn = 0, pp = 0
        
        mm = 0
        for nn in 0...g.size_y - 1 {
            for pp in 0...g.size_z {
                ey3[mm][nn][pp] = eyx0[nn][pp] +  abccoef * (ey3[mm + 1][nn][pp] - ey3[mm][nn][pp])
                eyx0[nn][pp] = ey3[mm + 1][nn][pp]
            }
        }
        
        for nn in 0...g.size_y {
            for pp in 0...g.size_z - 1 {
                ez3[mm][nn][pp] = ezx0[nn][pp] + abccoef * (ez3[mm + 1][nn][pp] - ez3[mm][nn][pp])
                ezx0[nn][pp] = ez3[mm + 1][nn][pp]
            }
        }
        
        mm = g.size_x - 1
        for nn in 0...g.size_y - 1 {
            for pp in 0...g.size_z {
                ey3[mm][nn][pp] = eyx1[nn][pp] + abccoef * (ey3[mm - 1][nn][pp] - ey3[mm][nn][pp])
                eyx1[nn][pp] = ey3[mm - 1][nn][pp]
            }
        }
            
        for nn in 0...g.size_y {
            for pp in 0...g.size_z - 1 {
                ez3[mm][nn][pp] = ezx1[nn][pp] + abccoef * (ez3[mm - 1][nn][pp] - ez3[mm][nn][pp])
                ezx1[nn][pp] = ez3[mm - 1][nn][pp]
            }
        }
            
        nn = 0
        for mm in 0...g.size_x - 1 {
            for pp in 0...g.size_z {
                ex3[mm][nn][pp] = exy0[mm][pp] + abccoef * (ex3[mm][nn + 1][pp] - ex3[mm][nn][pp])
                exy0[mm][pp] = ex3[mm][nn + 1][pp]
            }
        }
        
        for mm in 0...g.size_x {
            for pp in 0...g.size_z - 1 {
                ez3[mm][nn][pp] = ezy0[mm][pp] + abccoef * (ez3[mm][nn + 1][pp] - ez3[mm][nn][pp])
                ezy0[mm][pp] = ez3[mm][nn + 1][pp]
            }
        }
        
        nn = g.size_y - 1
        for mm in 0...g.size_x - 1 {
            for pp in 0...g.size_z {
                ex3[mm][nn][pp] = exy1[mm][pp] + abccoef * (ex3[mm][nn - 1][pp] - ex3[mm][nn][pp])
                exy1[mm][pp] = ex3[mm][nn - 1][pp]
            }
        }
            
        for mm in 0...g.size_x {
            for pp in 0...g.size_z - 1 {
                ez3[mm][nn][pp] = ezy1[mm][pp] + abccoef * (ez3[mm][nn - 1][pp] - ez3[mm][nn][pp])
                ezy1[mm][pp] = ez3[mm][nn - 1][pp]
            }
        }
        
        pp = 0
        for mm in 0...g.size_x - 1 {
            for nn in 0...g.size_y {
                ex3[mm][nn][pp] = exz0[mm][nn] + abccoef * (ex3[mm][nn][pp + 1] - ex3[mm][nn][pp])
                exz0[mm][nn] = ex3[mm][nn][pp + 1]
            }
        }
            
        for mm in 0...g.size_x {
            for nn in 0...g.size_y - 1 {
                ey3[mm][nn][pp] = eyz0[mm][nn] + abccoef * (ey3[mm][nn][pp + 1] - ey3[mm][nn][pp])
                eyz0[mm][nn] = ey3[mm][nn][pp + 1]
            }
        }
            
        pp = g.size_z - 1
        for mm in 0...g.size_x - 1 {
            for nn in 0...g.size_y {
                ex3[mm][nn][pp] = exz1[mm][nn] + abccoef * (ex3[mm][nn][pp - 1] - ex3[mm][nn][pp])
                exz1[mm][nn] = ex3[mm][nn][pp - 1]
            }
        }
            
        for mm in 0...g.size_x {
            for nn in 0...g.size_y - 1 {
                ey3[mm][nn][pp] = eyz1[mm][nn] + abccoef * (ey3[mm][nn][pp - 1] - ey3[mm][nn][pp])
                eyz1[mm][nn] = ey3[mm][nn][pp - 1]
            }
        }
    }
}
                
                





