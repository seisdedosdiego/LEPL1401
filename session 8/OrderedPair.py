def set_a(self, n_a):
    """ Spécification """
    self.p.a = n_a
    if self.p.a > self.p.b:
        self.ordered = False
    else:
        self.ordered = True
    
def set_b(self, n_b):
    """ Spécification """
    self.p.b = n_b
    if self.p.a > self.p.b:
        self.ordered = False
    else:
        self.ordered = True