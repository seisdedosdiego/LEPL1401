def recherche(m,v):
    """ Cette fonction retourne 'True' si l'entier v apparait dans la matrice m et 'False' sinon.
        pré: m une matrice (liste), et v un entier
        post: retourne false ou true en fonction de v et m
    """
    for i in m:
        for y in i:
            if y == v:
                return True
            else:
                pass
    return False   