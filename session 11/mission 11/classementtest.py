# Seisdedos Stoz Diego
# BARB27 - Equipe 11.74

import unittest
from classement import Classement
from coureur import Coureur
from resultat import Resultat
from temps import Temps

class ClassementTest(unittest.TestCase):
    def setUp(self):
        self.coureurs = [Coureur("Diego", 18),
                         Coureur("Arthur", 19),
                         Coureur("Marthe", 20)]

        self.temps1 = Temps(12)
        self.temps2 = Temps(13)
        self.temps3 = Temps(14)

        self.r1 = Resultat(self.coureurs[0], self.temps1)
        self.r2 = Resultat(self.coureurs[1], self.temps2)
        self.r3 = Resultat(self.coureurs[2], self.temps3)

        self.classement = Classement()

    def test_add(self):
        self.classement.add(self.r1)
        self.assertEqual(self.classement.get_position(self.coureurs[0]), 1)

        self.classement.add(self.r2)
        self.assertEqual(self.classement.get(self.coureurs[1]), self.r2)
        self.assertEqual(self.classement.get_position(self.coureurs[1]), 2)

        self.classement.add(self.r3)
        self.assertEqual(self.classement.get_position(self.coureurs[2]), 3)

    def test_get(self):
        self.classement.add(self.r2)
        self.assertEqual(self.r2, self.classement.get(self.coureurs[1]))
        self.classement.remove(self.coureurs[1])

    def test_remove(self):
        self.test_add()
        self.classement.remove(self.r2.coureur())
        self.assertEqual([self.r1, self.r3], self.classement.results().get_array())

if __name__ == "__main__":
    unittest.main()