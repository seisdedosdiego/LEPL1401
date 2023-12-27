def equal(l,d):
    """ Cette fonction détermine si d contient les mêmes valeurs que l pour chaque entrée de l.
        pré: l une liste et d un dictionnaire
        post: retourne True ou False
    """
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != d.get((i,j),0):
                return False
    return True