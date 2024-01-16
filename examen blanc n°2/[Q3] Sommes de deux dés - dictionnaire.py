def somme_des(n):
    """
    @pre:  n est un nombre entier > 0
    @post: retourne un dictionnaire avec comme différentes clés
           chaque somme possible des valeurs des dés,
           et comme valeur associée à cette clé e,
           la liste des tuples des valeurs des dés qui addtionnées donnent e
    """
    dict = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i+j) in dict:
                dict[(i+j)].append((i,j))
            else:
                dict[(i+j)] = [(i,j)]
    return dict

# ZONE TEST #
def test_somme_des():
    assert somme_des(4) == {2: [(1,1)], 3: [(1,2),(2,1)], 4: [(1,3),(2,2),(3,1)], 5: [(1,4),(2,3),(3,2),(4,1)], 6: [(2,4),(3,3),(4,2)], 7: [(3,4),(4,3)], 8: [(4,4)]}, "test 1"
    assert somme_des(6) == {2: [(1,1)], 3: [(1,2),(2,1)], 4: [(1,3),(2,2),(3,1)], 5: [(1,4),(2,3),(3,2),(4,1)],
6: [(1,5),(2,4),(3,3),(4,2),(5, 1)], 7: [(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)],
8: [(2,6),(3,5),(4,4),(5,3),(6,2)], 9: [(3,6),(4,5),(5,4),(6,3)],
10: [(4,6),(5,5),(6,4)], 11: [(5,6),(6,5)], 12: [(6,6)]}, "test 2"
    print("TOUT OK")

test_somme_des()