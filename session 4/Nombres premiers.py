def recherche(lst,v):
    for l in lst:
        if l == v:
            return True
        else:
                pass
    return False   

def primes(max):
    """ Cette fonction retourne une liste des nombres premiers jusque 'max' (inclu si max est un premier).
        Si max est négatif ou égale à 0, la liste est retournée vide.
        pré: max un entier positif
        post: un liste des nombres premiers avec max comme borne supérieur (inclu ou non).
    """
    if max<=0:
        return []
    if max == 1:
        return []
    else:
        nombres_premiers = []
        nombres_pas_premiers = []
        
        for i in range(2, max+1):
            for j in range(1, i):
                if i%j==0 and i!=j and j!=1:
                    nombres_pas_premiers.append(i)
                else:
                    pass
        nombres_pas_premiers = list(set(nombres_pas_premiers))
        
        for k in range(2, max+1):
            if recherche(nombres_pas_premiers, k) == False:
                nombres_premiers.append(k)
    
        nombres_premiers = list(set(nombres_premiers))
        return nombres_premiers