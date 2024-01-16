def get_carre_valeurs(self, x, y):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ x < N
           0 ≤ y < N
    @post: retourne une liste de toutes les valeurs apparaissant dans le SudokuCarre
           qui se trouve à la position (x, y) du puzzle Sudoku
           Si une valeur apparaît plusieurs fois dans ce carré,
           elle se retrouvera plusieurs fois dans la liste retournée.
    """
    list = []
    carre = self.get_carre(x,y)
    dimension = self.dimension
    for i in range(0,dimension):
        for j in range(0,dimension):
            list.append(carre.get_val(j,i))
    return list
    
def get_ligne(self, ligne):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ ligne < N * N
    @post: retourne une liste de toutes les valeurs apparaissant
           à une certaine ligne du puzzle Sudoku
           Si une valeur apparaît plusieurs fois sur une ligne
           elle se retrouvera plusieurs fois dans la liste retournée
    """
    l = ligne
    list = []
    dimension = self.dimension
    where = ligne//dimension
    while l>=dimension:
        l -= dimension
    for i in range(dimension):
        carre = self.get_carre(i,where)
        for j in range(dimension):
            list.append(carre.get_val(j,l))
    return list
        
def get_colonne(self, colonne):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ colonne < N * N
    @post: retourne une liste de toutes les valeurs apparaissant
           à une certaine colonne du puzzle Sudoku
           Si une valeur apparaît plusieurs fois sur une colonne
           elle se retrouvera plusieurs fois dans la liste retournée
    """
    c = colonne
    list = []
    dimension = self.dimension
    where = colonne//dimension
    while c>=dimension:
        c -= dimension
    for i in range(dimension):
        carre = self.get_carre(where,i)
        for j in range(dimension):
            list.append(carre.get_val(c,j))
    return list

# ZONE TEST #
p1 = create_valid_m()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 2 3
# 2 3 | 1 4

def test_get_carre_valeurs():
    assert p1.get_carre_valeurs(0, 0) == [1, 4, 3, 2], "test 1"
    assert p1.get_carre_valeurs(0, 1) == [4, 1, 2, 3], "test 2"
    assert p1.get_carre_valeurs(1, 0) == [3, 2, 4, 1], "test 3"
    assert p1.get_carre_valeurs(1, 1) == [2, 3, 1, 4], "test 4"
    print("TOUT OK - CARRE VALEURS")
    
def test_get_ligne():
    assert p1.get_ligne(0) == [1, 4, 3, 2], "test 1"
    assert p1.get_ligne(1) == [3, 2, 4, 1], "test 2"
    assert p1.get_ligne(2) == [4, 1, 2, 3], "test 3"
    assert p1.get_ligne(3) == [2, 3, 1, 4], "test 4"
    print("TOUT OK - LIGNE")

def test_get_colonne():
    assert p1.get_colonne(0) == [1, 3, 4, 2], "test 1"
    assert p1.get_colonne(1) == [4, 2, 1, 3], "test 2"
    assert p1.get_colonne(2) == [3, 4, 2, 1], "test 3"
    assert p1.get_colonne(3) == [2, 1, 3, 4], "test 4"
    print("TOUT OK - COLONNE")
    
test_get_carre_valeurs()
test_get_ligne()
test_get_colonne()