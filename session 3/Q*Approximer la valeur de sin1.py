def approx_sin(n):
    """
    @pre:   n est un entier tel que n >= 0
    @post:  retourne une estimation de sin 1 en sommant
    les n + 1 premiers termes de la série
    """
    sin_1 = 0
    for i in range(0, n+1):
        x = ((-1)**i)/(factorial(2*i+1))
        sin_1 += x
    return sin_1