def count(events, i, j):
    """ Cette fonction calcule le nombre de fois que la coordonnée '(i,j)' apparaît dans la liste 'events'.
        pré: events une liste de coordonnées, i et j des entiers.
        post: retourne le nombre de fois que la coordonnée est présente.
    """
    count = 0
    for k in events:
        if (i,j) == k:
            count += 1
            
    return count