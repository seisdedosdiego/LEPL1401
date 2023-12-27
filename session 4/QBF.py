def positions (p,s):
    """ pré : p est un pattern, c'est-à-dire une chaîne de caractères qui peut contenir des lettres,
        des chiffres et le caractère '?', s contient des lettres et des chiffres mais pas le caractère '?'
        
        post : retourne une liste des occurrences du pattern p à l'intérieur de la chaîne de caractères s
        une occurrence est une sous-chaîne de s de même longueur que p qui contient les mêmes caractères que p à toutes les positions,
        '?' peut remplacer tous les caractères en ignorant les majuscules et minuscules
    """
    positions = []
    p_low = p.lower()
    s_low = s.lower()
    len_s = len(s)
    len_p = len(p)
    
    for i in range(len_s - len_p + 1):
        x = True
        
        for j in range(len_p):
            if p_low[j] == "?":
                x = True
            elif p_low[j] == s_low[i+j]:
                x = True
            elif p_low[j] != s_low[i+j]:
                x = False
                break
            
        if x == True:
            positions.append(i)
    
    return positions