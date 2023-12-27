def house_designation(student_qualities):
    """ Cette fonction va retourner une liste avec les noms des quatres maisons, la première étant celle où l'étudiant devrait
        aller et la dernière, celle qui convient le moins à l'étudiant.
        pré: student_qualities une liste d'étudiants avec leurs qualités.
        post: une liste avec les 4 maisons.
    """
    gry_quali = 0
    rav_quali = 0
    huf_quali = 0
    sly_quali = 0
    
    list_exit = []
    
    for j in student_qualities:
        if j == "brave" or j == "strong" or j == "bold":
            gry_quali -=1
        elif j == "smart" or j == "wise" or j == "curious":
            rav_quali -= 1
        elif j == "loyal" or j == "patient" or j == "hard-working":
             huf_quali -= 1
        elif j == 'cunning' or j == 'wily' or j == 'malignant':
             sly_quali -= 1
        
    list_exit.append(gry_quali)
    list_exit.append(rav_quali)
    list_exit.append(huf_quali)
    list_exit.append(sly_quali)
    
    list_exit.sort()
    
    print(list_exit)
    length = len(list_exit)
    
    for i in range(length):
        print(i)
        if list_exit[i] == gry_quali:
            list_exit[i] = "Gryffindor"
            gry_quali = "stop"
            
        elif list_exit[i] == rav_quali:
            list_exit[i] = "Ravenclaw"
            rav_quali = "stop"
            
        elif list_exit[i] == huf_quali:
            list_exit[i] = "Hufflepuff"
            huf_quali = "stop"

        elif list_exit[i] == sly_quali:
            list_exit[i] = "Slytherin"
            sly_quali = "stop"
            
    
    return list_exit