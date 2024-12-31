PI = 3.14159265358979

def factorial(n):
    out = 1
    for i in range(2, n+1):
        out *= i
    return out

def cos(x : float, order : int = 30):
    out = 1
    signe = -1
    for k in range(2, order, 2):
        out += x**k / factorial(k) * signe
        signe = -signe
    return out

def sqrt(x):
    n = 1
    for i in range(20):
        n = (n + x/n) * 0.5
    return n

def sin(x : float, order : int = 30):
    #sin(x) = cos(x+PI/2)
    return cos(x + PI/2, order)

def theta(xi : float, xi1 : float, x : float):
    return (x - xi) / (xi1 - xi)

def hermite(point1 : tuple[float, float], point2 : tuple[float, float], prime1 : float, prime2 : float, x : float) -> float:
    t = theta(point1[0], point2[0], x)
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = -2*t**3 + 3*t**2
    h3 = t**3 - 2*t**2 + t
    h4 = t**3 - t**2

    return point1[1]*h1 + point2[1]*h2 + prime1*h3 + prime2*h4

def d_forward(point1 : tuple[float, float], point2 : tuple[float, float]):
    return (point1[1]-point2[1])/(point1[0]-point2[0])