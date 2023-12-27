def remove(self, cargo):
    previous = self.last()
    pointeur = self.first()
    if pointeur == None:
        return None
    elif previous is self.first() and pointeur.value() == cargo:
        self.__first = None
        self.__last = None
        pointeur.set_next(None)
        return pointeur
    else:
        while True : 
            if pointeur.value() == cargo:
                previous.set_next(pointeur.next())
                if pointeur is self.first():
                    self.__first = previous.next()
                if pointeur is self.last():
                    self.__last = previous
                pointeur.set_next(None)
                return pointeur
            previous = pointeur
            pointeur = pointeur.next()
            if pointeur is self.first():
                break
                
def removeAll(self, cargo):
    while True :
        if self.remove(cargo) is None:
            break