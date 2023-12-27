class Student:
    noma = 0
    def __init__(self, prenom, nom, date, courriel):
        self.prenom = prenom
        self.nom = nom
        self.date = date
        self.courriel = courriel
        self.nomax = str(Student.noma)
        Student.noma += 1
    def __str__(self):
        return f"L'étudiant numéro {self.nomax} : {self.prenom} {self.nom} né le {str(self.date)}, peut être contacté par {self.courriel}"