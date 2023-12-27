def chiffres_pairs(n):
    """ Cette fonction renvoit true lorsque n possède un nombre paire de chiffres dans sa représentation décimale.
    
        pré: n est un int positif
        post: renvoit true or false en fonction du nombre
    """
    n = str(n)
    if (len(n)%2==0):
        return True
    else:
        return False