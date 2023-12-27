""" Cette fonction retourne une liste avec le classement des coureurs par ordre croissant du temps venant des 2 listes distinctes.
    pré: first_list et second_list des listes.
    post: une liste avec les éléments des 2 listes dans l'ordre.
"""
lst = []  
for i in first_list:
    lst.append(i)
length_1 = len(lst)
length_2 = len(second_list)
for j in range(0, length_2): 
    for k in range(0, length_1):     
        if second_list[j][1] < lst[k][1]:
            lst.insert(k, second_list[j])
            length_1 +=1
            break
        elif second_list[j][1] == lst[k][1]:
            lst.insert(k+1, second_list[j])
            length_1 +=1
            break   
        elif lst[k][1] < second_list[j][1] < lst[k+1][1]:
            lst.insert(k+1, second_list[j]) 
            length_1 +=1
            break            
        elif lst[length_1-1][1]< second_list[j][1]:
            lst.insert(length_1+length_2-1, second_list[j])
            length_1 +=1
            break                
        else:
            pass
return lst