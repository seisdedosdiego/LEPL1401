def treatment(data):
    """ Cette fonction complète la fonction précédente (extract) en ajoutant '*' et un nombre pour les répétitions.
        pré: data une chaîne de caractères.
        post: une chaîne de caractères modifiée.
    """
    lst = data.split(" ")
    new_data = [[lst[0], 1]]
    
    for i in lst[1:]:
        if i == new_data[-1][0]:
            new_data[-1][1] +=1
        elif i == "":
            pass
        else:
            new_data.append([i,1])
    
    for j,k in enumerate(new_data):
        new_data[j][1] = str(k[1])
    x = []
    for m in new_data:
        x.append("*".join(m))
    return " ".join(x)   