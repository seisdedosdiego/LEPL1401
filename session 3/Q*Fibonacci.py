def fibonacci(n):
    """ Cette fonction retourne le Nième élément de la suite de fibonacci."""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(0,n-1):
            x = a + b
            a = b
            b = x
        return x