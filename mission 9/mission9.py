# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74



########## CLASS ARTICLE ##############
class Article :

    def __init__(self,d,p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p
        
    def description(self) :
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) :
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """    
        return 0.21

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())
########## FIN CLASS ARTICLE ##########



########## CLASS FACTURE ##############
class Facture :

    def __init__(self, d, a_list, num_uni = 297247):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.__num_uni = num_uni

    def num_uni(self):
        return self.__num_uni
        
    def description(self) :
        """
        @post: retourne la description de cette facture.
        """
        return self.__description
    
    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Facture " + "No " + str(self.num_uni()) + " : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<39}  | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
               + self.barre_str()
            
    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
               + self.barre_str()
            
    def nombre(self, pce) :
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        count = 0
        for piece in self.__articles():
            if ArticlePiece.piece == pce:
                count += 1
            else:
                pass 
        return count
   
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = "Livraison - Facture " + "No " + str(self.num_uni()) + " : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<39}  | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids") \
               + self.barre_str()
        count = 0
        totalnombre = 0.0
        totalpoids = 0.0
        fra = False
        for art in self.__articles :
            if isinstance(art, ArticlePiece):
                if art.piece().fragile() == False:  
                    s += "| {0:40} | {1:8.3f}kg | {2:10} | {3:8.3f}kg |\n".format(art.description2(), art.piece().poids(), art.number() ,art.piece().poids()*art.number())
                    totalnombre += art.number()
                    totalpoids += art.piece().poids()*art.number()
                    count += 1
                else:
                    descri = art.description2() + " (!)"
                    s += "| {0:40} | {1:8.3f}kg | {2:10} | {3:8.3f}kg |\n".format(descri, art.piece().poids(), art.number() ,art.piece().poids()*art.number())
                    totalnombre += art.number()
                    totalpoids += art.piece().poids()*art.number()
                    count += 1
                    fra = True
            else: 
                pass 
        total_article = str(count) + " articles"
        s += self.barre_str() \
               + "| {0:40} | {1:10.2} | {2:10} | {3:8.3f}kg |\n".format(total_article, "  ", int(totalnombre), totalpoids) \
               + self.barre_str()
        if fra == True:
            s += " (!) *** livraison fragile *** \n" 
        return s
########## FIN CLASS FACTURE ########



##### CLASS ARTICLE REPARATION #######
class ArticleReparation(Article):
    
    def __init__(self, reparation_duree):
        if type(reparation_duree) == float:
            self.reparation_duree = reparation_duree
        else:
            print("Erreur au niveau des types des arguments")
    
    def description(self):
        description = f"Reparation ({self.reparation_duree} heures)"
        return description
    
    def prix(self):
        
        prix = 20 + 35*(self.reparation_duree)
        return prix
###### FIN CLASS ARTICLE REPARATION #####



############ CLASS PIECE ################
class Piece:

    def __init__(self, description, prix, poids = 0, fragile = False, tva_reduit = False):
        self.__description = description
        self.__prix = prix
        self.__poids = poids
        self.__fragile = fragile
        self.__tva_reduit = tva_reduit
    
    def description(self):
        return self.__description
    
    def prix(self):
        return self.__prix
    
    def poids(self):
        return self.__poids
    
    def fragile(self):
        return self.__fragile
    
    def tva_reduit(self):
        return self.__tva_reduit
    
    def __eq__(self, piece):
        if self.description() == piece.description() and self.__prix == piece.prix():
            return True
        else: 
            return False
######### FIN CLASS PIECE ################



###### CLASS ARTCILE PIECE ###############
class ArticlePiece(Article):

    def __init__(self,number, piece):
        self.__number = number
        self.__piece = piece

    def number(self):
        return self.__number
    
    def piece(self):
        return self.__piece
    
    def description(self):
        return f"{self.number()} * {self.piece().description()} @ {self.piece().prix()}"
    
    def description2(self):
        return f"{self.piece().description()} @ {self.piece().prix()}"
    
    def prix(self):
        return (self.piece().prix())*(self.number())
    
    def taux_tva(self):
        if self.piece().tva_reduit() == True:
            return (6/100)
        elif self.piece().tva_reduit() == False:
            return (21/100)
###### FIN CLASS ARTCILE PIECE ###########



if __name__ == "__main__":
    
    #a = ArticleReparation(1.0)
    #print(a.prix())
    p1 = Piece("p1", 10.0)
    a1 = ArticlePiece(5, p1)
    

    articles1 = [ 
             Article("laptop 15\" 8GB RAM", 743.79),
             ArticlePiece(1, Piece("disque dur 350 GB", 49.99, 0.355, fragile = True, tva_reduit=True)),
             ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.176)),
             ArticlePiece(5, Piece("adaptateur DVI - VGA", 12.00, 0.000)),
             ArticlePiece(2, Piece("Java in a Nutshell", 24.00, 0.321)),
             ArticlePiece(5, Piece("souris bluetooth", 15.99, 0.176)),
             ]
    x = Facture("PC Store - 22 novembre", articles1, 696969)
    print(x.livraison_str())
