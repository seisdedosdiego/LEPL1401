class CD(Item):
    serial = 100000
    
    def __init__(self, auteur, titre, duree):
        super().__init__(auteur, titre, CD.serial)
        self.__duree = duree
        CD.serial += 1
        
    def duree(self):
        return self.__duree
        
    def __str__(self):
        x = f" ({self.duree()} s)"
        return super().__str__() + x