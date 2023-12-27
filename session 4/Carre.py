def carre(n):
    """ Cette fonction retourne un matrice 'spéciale'.
        pré: n un nombre entier donné
        post: retourne une matrice 'spéciale'
    """
    my_matrice = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(j+i*n)
        my_matrice.append(row)
    return my_matrice