def binary_search ( course, list_of_courses ):
    """ Cette fonction retourne tous les étudiants d'un cours donné à l'aide d'une liste courses.
        pré: course un cours, list_of_courses une liste avec les cours et leurs élèves.
        post: retourne le nom des étudiants du cours, ou une liste vide si le cours n'existe pas ou s'il n'y a pas d'étudiant.
    """
    first = 0
    last = len(list_of_courses)-1
    found = False

    while first<=last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][0] == course:
            found = True
            index_course = middle
        else:
            if course < str(list_of_courses[middle][0]):
                last = middle-1
            else:
                first = middle+1
    
    if found == True:
        list_stu = list_of_courses[middle][1]
    else:
        list_stu = []
    
    return list_stu