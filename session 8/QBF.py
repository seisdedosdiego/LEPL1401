class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
    def augmente(self, augmentation):
        self.salaire += augmentation
    def __str__(self):
        return self.nom + " : " + str(self.salaire)