def __eq__(self,p):
    """
    @pre: -
    @post: Retourne true si la paire p est égale à l'objet.
           Retourne false sinon
    """  
    if type(p) is Pair:
        return self.a == p.a and self.b == p.b
    return False