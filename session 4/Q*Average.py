""" Cette fonction retourne la moyenne arithmétique des éléments contenu dans la list.
    Si la list est vide elle retourne 'None'.
    pré: lsit une liste
    post: retourne une moyenne arithémtique
"""
org_lst = []
if list == []:
    return None
else: 
    for i in list:
        if type(i) == int or type(i) == float:
            org_lst.append(i)
        else:
             pass
            
length = len(org_lst)
sum_lst = 0
    
for j in org_lst:
    if type(j) == int:
        j = float(j)
        sum_lst += j
    elif type(j) == float:
        sum_lst += j
            
arith = sum_lst/length

    
return arith