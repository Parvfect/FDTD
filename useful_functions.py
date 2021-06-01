

def mqn(m:Int, q:Int, n:Int):
    return m * 6 + q + 3 * n


def nqm(n:Int, q:Int, m:Int) :
    return mqn(m:n, q:q, n:m)


def ngp(n: Int, g:Int, p: Int):
    return (n * g) + p


def intInput():
    return Int(input())

