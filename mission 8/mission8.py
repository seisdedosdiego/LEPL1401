# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74
# Fait avec Adrien Sillis


### CLASS DUREE ###

class Duree:
    
    def __init__(self, h, m, s):
        """
        pre: h, m et s sont des entiers positifs (ou zéro)
              m et s sont < 60
        post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        if not 0 <= s < 60:
            m += s//60
            s %= 60
        if not 0 <= m < 60:
            h += m//60
            m %= 60
        self.heure = h
        self.minute = m
        self.seconde = s
        
        #if type(h) == int and type(m) == int and type(s) == int and 0 <= s <60 and 0 <= m <60 and 0 <= h:
            
           # self.heure = h
           # self.minute = m
           # self.seconde = s
            
        #else:
          #  raise ValueError ("An error occured w/ the arguments")
            
    def to_secondes(self):
        """
        pre: /
        post: Retourne le nombre total de secondes de cette instance de Duree (self).
              Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        
        h_in_s = (self.heure)*60*60
        m_in_s = (self.minute)*60
        s_in_s = self.seconde
        total_secondes = s_in_s + m_in_s + h_in_s
        
        return total_secondes
    
    
    def delta(self,d) :
        """
        pre:  d est une instance de la classe Duree
        post: Retourne la différence en secondes entre cette durée (self)
              et la durée d passée en paramètre.
              Cette valeur renovoyée est positif si cette durée (self)
              est plus grand que la durée d, négatif sinon.
              Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
              et la durée d est 0h 1m 25s, la valeur retournée est 31200.
              Inversement, si cette durée (self) est 0h 1m 25s et la durée
              d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        delta = self.to_secondes() - d.to_secondes()
        
        return delta
    
    def apres(self,d):
        """
        pre: d est une instance de la classe Duree
        post: Retourne True si cette durée (self) est plus grand que la durée
              d passée en paramètre; retourne False sinon.
        """
        if self.delta(d) > 0:
            return True
        else:
            return False

    def ajouter(self,d):
        """
        pre: d est une instance de la classe Duree
        post: Ajoute une autre durée d à cette durée (self),
              corrigée de manière à ce que les minutes et les secondes soient
              dans l'intervalle [0..60[, en reportant au besoin les valeurs
              hors limites sur les unités supérieures
              (60 secondes = 1 minute, 60 minutes = 1 heure).
              Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        self.seconde += d.seconde
        self.minute += d.minute
        self.heure += d.heure
        if not 0 <= self.seconde < 60:
            self.minute += self.seconde//60
            self.seconde %= 60
        if not 0 <= self.minute < 60:
            self.heure += self.minute//60
            self.minute %= 60
        
        #total = d.to_secondes() + self.to_secondes()
        #self.heure = total//3600
        #self.minute = (total%3600)//60
        #self.seconde = (total%3600)%60
        
    def __str__(self):
        """
        pre: /
        post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
               Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
               retourne le string désiré avec les nombres en deux chiffres en ajoutant
               les zéros nécessaires.
        """
        duree = "{:02}:{:02}:{:02}".format(self.heure, self.minute, self.seconde)
        
        return duree

### CLASS CHANSON ###

class Chanson:
    
    def __init__(self,t,a,d):
        """
        pre: t et a sont des string, d est une instance de la classe Duree
        post: Crée une nouvelle chanson, caractérisée par un titre t,
              un auteur a et une durée d.
        """
        if type(t) == str and type(a) == str:
            
            self.titre = t
            self.auteur = a
            self.duree = d
    
        else:
            raise ValueError ("An error occured w/ the arguments")
             
    def __str__(self):
        """
        pre:  -
        post: Retourne un string décrivant cette chanson sous le format
              "TITRE - AUTEUR - DUREE".
              Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        description = str(self.titre) + " - " + str(self.auteur) + " - " + self.duree.__str__()
        return description
        
### CLASS ALBUM ###

class Album:
    
    def __init__(self, numero):
        """
        pre:  numero est un entier identifiant de facon unique cet album
        post: Crée un nouvel album, avec comme identifiant le numero,
              et avec une liste de chansons vide.
        """
        if type(numero) == int:
            self.identifiant = numero
            self.ls_chanson = []
            
            self.duree = 0
            self.heure = 0
            self.minute = 0
            self.seconde = 0
        else:
            raise ValueError ("An error occured w/ the arguments")
        
    def add(self, chanson):
        """ Spécification """
        
        if len(self.ls_chanson) < 99 and (self.duree + chanson.duree.to_secondes()) <= (75*60):
            self.ls_chanson.append(chanson)
            self.duree += chanson.duree.to_secondes()
            return True
        
        else:
            return False
        
    def __str__(self):
   
        self.heure = (self.duree)//3600
        self.minute = ((self.duree)%3600)//60
        self.seconde = ((self.duree)%3600)%60
        
        x = Duree(self.heure, self.minute, self.seconde)
        y = x.__str__()
        
        retour = ""
        
        line1 = "Album " + str(self.identifiant) + " (" + str(len(self.ls_chanson)) + " chansons" + ", " + str(y) + ")" + "\n"
        
        retour += line1
        
        for i in range(1, len(self.ls_chanson)+1):
            if i < 10:
                descript = self.ls_chanson[i-1].__str__()
                line = "0" + str(i) + ": " + descript + "\n"
                retour += line
            else:
                descript = self.ls_chanson[i-1].__str__()
                line = str(i) + ": " + descript + "\n"
                retour += line
            
        return retour.strip()
        
### LE PROGRAM ###

def program():
    
    with open ("music-db.txt", "r") as f:
        
        counter = 1
        album = Album(counter)
        
        for line in f:
            
            ls = line.split(" ")
            title = ls[0]
            author = ls[1]
            time_min = int(ls[2])
            time_sec = int(ls[3])
            time = Duree(0, time_min, time_sec)
            song = Chanson(title, author, time)
            
            if album.add(song) == True:
                pass
            
            elif album.add(song) == False:
                print(album.__str__() + "\n")
                counter += 1
                album = Album(counter)
                album.add(song)
                
        print(album.__str__().strip())
        
if __name__ == "__main__":   
    program()
    