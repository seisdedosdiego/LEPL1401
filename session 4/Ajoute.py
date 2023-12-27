def ajoute(l, v):
    """ Cette fonction ajoute le nombre v à la fin de la liste l si ce nombre n'est pas encore présent dans la liste.
        pré: l une liste et v un nombre
        post: une liste avec peut-être le nombre à la fin
    """
    stock = 0
    for i in l: 
        if i == v:
            stock = 0
            break
        else:
            stock = v
            
    if stock == v:
        l.append(v)