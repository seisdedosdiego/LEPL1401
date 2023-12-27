# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74

from mission9 import Article, Facture, ArticleReparation, Piece, ArticlePiece

###############################################################
articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49),
             ArticleReparation(0.75),
             ArticlePiece(5, Piece("piece1", 9.99,tva_reduit=True)),
             ArticlePiece(10, Piece("piece2", 4.99)),
             ]
articles1 = [ 
             Article("laptop 15\" 8GB RAM", 743.79),
             ArticlePiece(1, Piece("disque dur 350 GB", 49.99, 0.355, fragile = True, tva_reduit=True)),
             ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.176)),
             ArticlePiece(5, Piece("adaptateur DVI - VGA", 12.00, 0.000)),
             ArticlePiece(2, Piece("Java in a Nutshell", 24.00, 0.321)),
             ArticlePiece(5, Piece("souris bluetooth", 15.99, 0.176)),
             ]
facture = Facture("PC Store - 22 novembre", articles, num_uni = 923829 )
facture1 = Facture("PC Store - 22 novembre", articles1, num_uni = 696969 )
r1 = ArticleReparation(1.0)
p1 = Piece("piece1", 9.99,tva_reduit=True)
p2 = Piece("piece2", 4.99)
a1 = ArticlePiece(5, p1)
a2 = ArticlePiece(10, p2)
###############################################################


### Test Class Articles ###

def test_articles(a_list) :
    for art in a_list :
        print(art)

### Test Class Facture ###

def test_facture(f) :
    print(f)

### Test Class ArticleReparation ###

def test_ArticleReparation():

    assert r1.description() == "Reparation (1.0 heures)", "test 1"
    assert r1.prix() == 55.0, "test 2"
    print("All good !")
    
### Test Class Piece ###

def test_Piece():

    assert p1.description() == "piece1", "test 1"
    assert p1.prix() == 9.99, "test 2"
    assert p1.tva_reduit() == True, "test 3"
    assert p1.__eq__(p2) == False, "test 4"
    print("Tout bien !")

### Test Class ArticlePiece ###

def test_ArticlePiece():

    assert a1.number() == 5, "test 1"
    assert a2.description() == "10 * piece2 @ 4.99", "test 2"
    assert a1.prix() == 49.95, "test 3"
    assert a1.taux_tva() == 6/100, "test 4"
    assert a2.taux_tva() == 21/100, "test 5"
    print("Alles gut ! ")



if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)

    print("\n*** TEST DE LA CLASSE Facture - LIVRAISON ***\n")
    test_facture(facture1.livraison_str())
    
    print("*** TEST DE LA CLASSE ArticleReparation ***\n")
    test_ArticleReparation()

    print("\n*** TEST DE LA CLASSE Piece ***\n")
    test_Piece()

    print("\n*** TEST DE LA CLASSE ArticlePiece ***\n")
    test_ArticlePiece()

    


