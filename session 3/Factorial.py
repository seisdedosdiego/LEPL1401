def fact(n):
    """pré: n est un int
       post: retourne la factorielle de n
    """
    factorielle = 1
    for i in range(n, 0, -1):
        factorielle = factorielle*i
    return factorielle