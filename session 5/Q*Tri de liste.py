def list_sort(a_list):
    """ Cette fonction trie les listes qui lui sont données.
        pré: a_list une liste
        post: retourne une liste trier avec tout les éléments de a_list
    """
    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if a_list[i] <= a_list[j]:
                a_list[i], a_list[j]= a_list[j], a_list[i]
    #sorted_list = a_list
    return a_list

sorted_list = list_sort(a_list)