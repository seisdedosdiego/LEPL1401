def cross(trace1,trace2,theta1,theta2):
    """
    pre :  deux traces trace1 et trace2, chacun une liste de tuples (t,(x,y)),
           deux floats theta1 et theta2
    post : retourne 1 si les traces trace1 et trace2 se croisent, ou theta1 et
           theta2 sont utilisés comme seuils, comme indiqué dans les consignes
           de l'exercice.
           0, sinon
    """
    len1 = len(trace1)
    len2 = len(trace2)
    
    for i in range(len1):
        for j in range(len2):
            
            if absolute(trace1[i][0], trace2[j][0]) <= theta1 and euclidian_distance(trace1[i][1], trace2[j][1]) < theta2:
                return 1
            else:
                pass
    
    return 0 