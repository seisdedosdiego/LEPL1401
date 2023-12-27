def solveur(ls):
    """ Cette fonction retourne les solutions d'équations (reçu sous forme de listes) dans une liste.
        pré: ls une liste de listes sous forme [a,b,c].
        post: retourne les solutions des équations.
    """
    sol = []
    sol_n = []
    if ls == []:
        return sol
    else: 
        for i in ls:
            sol_n = solution(i[0], i[1], i[2])
            sol.append(sol_n)
    return sol