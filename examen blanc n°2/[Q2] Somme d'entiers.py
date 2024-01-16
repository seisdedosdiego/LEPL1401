def combien(n):
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d’entiers consecutifs
           strictement positifs dont la somme est egale a n
    """
    count = 0
    for i in range(1,n+1):
        sum = 0
        x = i
        while sum<n:
            sum +=x
            if sum == n:
                count += 1
            x += 1
    return count

# ZONE TEST #
def test_combien():
    assert combien(100) == 3, "test 1"
    assert combien(5) == 2, "test 2"
    assert combien(10) == 2, "test 3"
    assert combien(6) == 2, "test 3"
    print("TOUT OK")

test_combien()