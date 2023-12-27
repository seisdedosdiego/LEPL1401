def rho(a,b,c):
    """ Cette fonction calcule le déterminant d'une équation type : ax^2 + bx + c = 0.
        pré: a, b, c des réels
        post: retourne la valeur du déterminant
    """
    x = (b**2)-4*a*c
    return x

def n_solutions(a,b,c):
    """ Cette fonctions calcule le nombre de solutions d'une équation en fonction de son déterminant.
        pré: a, b, c des réels
        post: retourne le nombre de solutions de l'équation
    """
    x = rho(a,b,c)
    if x>0:
        return 2
    elif x==0:
        return 1
    else:
        return 0
    
def solution(a,b,c):
    """ Cette fonction calcule la valeur de la solution d'une équation de type : ax^2 + bx + c = 0.
        Elle retourne une solution (la plus petite) si le déterminant est plus grand que 0. 
        Elle ne peut pas être appelée pour une équation qui possède un déterminant égal à 0.
        
        pré: a, b, c des réels
        post: Elle retourne la valeur des solutions de l'équation.
    """
    x = rho(a,b,c)
    if x>0:
        solution_1 = (-b + racine_carree(x))/(2*a)
        solution_2 = (-b - racine_carree(x))/(2*a)
        if solution_1 > solution_2:
            return solution_2
        else:
            return solution_1
    else:
        solution_0 = (-b/(2*a))
        return solution_0