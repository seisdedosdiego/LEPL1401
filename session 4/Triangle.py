def triangle(n):
    """ Cette fonction returne une liste de listes imbriquées. 
        pré: n un entier
        post: retourne une liste de listes imbriquées
    """
    ls_2 = []
    ls_1 = []
    for i in range(0, n+1):
        ls_1 = ls_1 + [i]
        ls_2.append(ls_1)
    return ls_2