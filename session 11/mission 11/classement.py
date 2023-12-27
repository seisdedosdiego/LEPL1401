# Seisdedos Stoz Diego
# BARB27 - Equipe 11.74

from orderedlinkedlist import OrderedLinkedList

class Classement :
    __maxcapacity = 10

    def __init__(self):
      
        self.__resultats = OrderedLinkedList([])

    def size(self):

        return self.__resultats.size()
        
    def results(self): # nouvelle méthode

        return self.__resultats

    def add(self,r): # méthode modifiée

        self.__resultats.add(r)

    def get(self,c): # méthode modifiée
        
        node = self.__resultats.first()
        while node is not None:
            if node.value().coureur() == c:
                return (node.value())
            node = node.next()

    def get_position(self,c): # méthode modifiée
        
        node = self.__resultats.first()
        i = 1
        while node is not None:
            if node.value().coureur() == c:
                return i
            i += 1
            node = node.next()
        return -1

    def remove(self,c): # méthode modifiée
        
        node = self.__resultats.first()
        previous = node
        while node is not None:
            if node.value().coureur() == c:
                if node == self.__resultats.first():
                    self.__resultats.remove()
                    return c
                else:
                    previous.set_next(node.next())
                    self.__resultats.dec_size()
                    return c
            previous = node
            node = node.next()
        return False

    def __str__(self):
        
        s = ""
        d = self.__resultats.get_array()
        for c in d:
            s += "  " + str(self.get_position(c.coureur())) + " > " + str(c.coureur()) + "\n"
        return s
    
