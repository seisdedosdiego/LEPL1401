def is_adn(s):
    """ Cette fonction prend une chaîne de caractère, et renvoit 'True' si elle ne contient que des caractères
        tels que a, t, c, g et 'False' dans le cas contraire.
        pré: s une chaîne de caractère
        post: retourne 'True' ou 'False' en fonction de la chaîne de caractère
    """
    sequence = s.lower()
    longueur = int(len(sequence))
    test = 0
    
    for i in sequence:
        if i=="a" or i=="t" or i=="c" or i=="g":
            test += 1
        else:
            pass
        
    if longueur == test:
        return True
    else:
        return False

    
def positions(s, p):
    """ Cette fonction retourne les positions des occurences de p dans s.
        pré: s et p deux chaînes de caractères
        post: retourne les positions d'occurences de p dans s
    """
    s = s.lower()
    p = p.lower()
    x = len(s)
    y = len(p)
    stockage = []
    
    for i in range(0, x-y+1):
        if s[i:i+y] == p:
            stockage.append(i)
            
    return stockage


def distance_h(c_1, c_2):
    """ Cette fonction calcule la distance de Hamming entre 2 chaînes de caractères de longueurs égales.
        pré: c_1 et c_2 des chaînes de caractères de longueur égale.
        post: retourne la distance de Hamming
    """
    c_1 = c_1.lower()
    c_2 = c_2.lower()
    len_1 = len(c_1)
    len_2 = len(c_2)
    distance_hamming = 0
    if len_1 != len_2:
        return None
    else:
        x = -1
        for i in c_1:
            x += 1
            if i == c_2[x]:
                pass
            else:
                distance_hamming +=1
    
    return distance_hamming

print(distance_h('FDYu1','FdsJz'))

def distances_matrice(l):
    """ Cette fonction calcule une matrice des distances de Hamming entre toutes les chaînes de caratères de la liste.
        pré: l une liste de chaînes de caractères
        post: retourne une matrice des distances de Hamming
    """
    matrice = []
    row = []
    x = 0
    for i in l:
        for j in l:
            row.append(distance_h(i,j))
        matrice.append(row)
        row = []
        
    return matrice

#print(distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ]))