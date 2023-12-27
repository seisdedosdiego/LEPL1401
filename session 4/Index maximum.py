def maximum_index(lst):
    """ Cette fonction retourne l'index de l'élément avec la plus grande valeur d'une liste non vide.
        pré: lst une liste non vide
        post: retourne l'index de l'élément
    """
    ind = 0
    for i in lst:
        for j in lst:
            if i==j:
                pass
            elif i<j:
                pass
            elif i>j and i>ind:
                ind = i
                
    return lst.index(ind)