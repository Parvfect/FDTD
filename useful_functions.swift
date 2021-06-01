
import Foundation

public func make1DArray(size:Int) -> [Double]{
    return Array(Array(repeating: 0.0, count: size))
}

public func make2DArray(x:Int, y:Int) -> [[Double]]{
    var arr_2D = [[Double]]()
    var arr = [Double]()
    
    for _ in 0...x{
        for _ in 0...y{
            arr.append(0)
        }
        arr_2D.append(arr)
        arr = []
    }
    
    return arr_2D
    
}

public func make3DArray(x:Int, y:Int, z:Int) -> [[[Double]]]{
    var arr_2D = [[Double]]()
    var arr = [Double]()
    var arr_3D = [[[Double]]]()
    
    for _ in 0...x{
        for _ in 0...y{
            for _ in 0...z{
                arr.append(0.0)
            }
            arr_2D.append(arr)
            arr = [Double]()
        }
        arr_3D.append(arr_2D)
        arr_2D = [[Double]]()
    }
    
    
    return arr_3D
}

public func mqn(m:Int, q:Int, n:Int) -> Int{
    return m * 6 + q + 3 * n
}

public func nqm(n:Int, q:Int, m:Int) -> Int {
    return mqn(m:n, q:q, n:m)
}

public func ngp(n: Int, g:Int, p: Int) -> Int{
    return (n * g) + p
}

public func intInput() -> Int{
    return Int(readLine(strippingNewline: true)!)!
}
