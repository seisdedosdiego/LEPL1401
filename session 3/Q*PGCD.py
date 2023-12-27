def gcd(a,b):
    """ Retourne le PGCD de a et b. 
        pré: a et b sont des nombres naturels
        post: retourne le PGCD de a et b
    """
    if a==b: 
        return a
    elif a==0 and b>0:
        return b
    elif b==0 and a>0:
        return a
    else: 
        if a>b:
            for i in range(b, 0, -1):
                if a%i==0 and b%i==0: 
                    return i
        else: 
            for i in range(a, 0, -1):
                if b%i==0 and a%i==0: 
                    return i