def mix(l):    # Ne pas effacer cette ligne
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d’entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    list = []
    l_inverse = []
    for i in l:
        l_inverse.append(i)
    l_inverse.reverse()
    for i in range(len(l)//2):
        list.append(l[i])
        list.append(l_inverse[i])
    return list

# ZONE TEST #
def test_mix():
    assert mix([1,2,3,4]) == [1, 4, 2, 3], "test 1"
    assert mix([1,2,1,2,1,2]) == [1,2,2,1,1,2], "test 2"
    assert mix([0,0,0,0]) == [0,0,0,0], "test 3"
    assert mix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1,10,2,9,3,8,4,7,5,6], "test 4"
    print("TOUT OK")

test_mix()