""" Cette fonction calcule la somme des éléments contenus dans la liste.
    pré: list une liste
    post: retourne la somme des éléments (qui sont des nombres)
"""
org_lst = []
sum_lst = 0.0
x = 0
if list == []:
    return 0
for i in list:
    if type(i) == int or type(i) == float:
        org_lst.append(i)
    else:
        pass
    
for j in org_lst:
    if type(j) == int:
        x = 1
        j = float(j)
        sum_lst += j
    elif type(j) == float:
        x = 2
        sum_lst += j

if x==1:
    sum_lst = int(sum_lst)
    return sum_lst
elif x==2:
    return sum_lst