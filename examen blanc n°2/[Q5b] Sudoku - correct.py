def est_correct(self):    # Ne pas effacer cette ligne
    """
    @pre:  ce Sudoku est bien formé, de dimension self.dimension
    @post: retourne un booléen
           True si le puzzle est correct
           False sinon
    """
    dimension = self.dimension
    dimension2 = dimension**2
    we_want = []
    for i in range(1,dimension**2+1):
        we_want.append(i)
    for i in range(dimension):
        for j in range(dimension):
            carre = self.get_carre_valeurs(i,j)
            carre2 = sorted(carre)
            if carre2 != we_want:
                return False
    for i in range(dimension2):
        ligne = self.get_ligne(i)
        ligne2 = sorted(ligne)
        if ligne2 != we_want:
            return False
    for i in range(dimension2):
        colonne = self.get_colonne(i)
        colonne2 = sorted(colonne)
        if colonne2 != we_want:
            return False
    return True

# ZONE TEST #
p1 = create_correct_m()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 2 3
# 2 3 | 1 4

p2 = create_not_correct_col()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 3 2
# 2 3 | 4 1

p3 = create_not_correct_line()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 1 4
# 2 3 | 2 3

p4 = create_not_correct_square()
# 3 1 | 4 2
# 2 3 | 1 4
# ---------
# 1 4 | 2 3
# 4 2 | 3 1

p5 = create_correct_m()

def test_est_correct():
    assert p1.est_correct() == True, "test 1"
    assert p2.est_correct() == False, "test 2"
    assert p3.est_correct() == False, "test 3"
    assert p4.est_correct() == False, "test 4"
    assert p5.est_correct() == True, "test 5"
    print("TOUT OK")