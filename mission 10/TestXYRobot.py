# Seisdedos Stoz Diego 
# BARB27 - Equipe 11.74

from XYRobot import XYRobot as XYRob
import unittest
# import time

class TestXYRobot(unittest.TestCase):
    def setUp(self):
        self.robot1 = XYRob("R2-D2", x=100, y=100)

    def test_str(self):
        self.assertEqual(self.robot1.__str__(), "R2-D2@(100,100) angle: 0.0")
    
    def test_nom(self):
        self.assertEqual(self.robot1.nom(), "R2-D2")

    def test_x(self):
        self.assertEqual(self.robot1.x(), 100)
    
    def test_y(self):
        self.assertEqual(self.robot1.y(), 100)
    
    def test_angle_rad(self):
        self.assertEqual(self.robot1.angle_rad(), 0)
        #time.sleep(5)

    def test_angle(self):
        self.assertEqual(self.robot1.angle(), 0)
        #time.sleep(5)

    # pas de test pour __set_x car c'est une méthode privée

    # pas de test pour __set_y car c'est une méthode privée

    # pas de test pour __set_angle_rad car c'est une méthode privée

    def test_position(self):
        self.assertEqual(self.robot1.position(), (100,100))

    # pas de test pour __draw_from car c'est une méthode privée

    # pas de test pour __move car c'est une méthode privée

    def test_move_forward(self):
        self.robot1.move_forward(50)
        self.assertEqual(self.robot1.__str__(), "R2-D2@(150,100) angle: 0.0")
        self.robot1.move_backward(50) # je remet le robot au bon endroit pour les autres tests

    def test_move_backward(self):
        self.robot1.move_backward(50)
        self.assertEqual(self.robot1.__str__(), "R2-D2@(50,100) angle: 0.0")
        self.robot1.move_forward(50) # je remet le robot au bon endroit pour les autres tests
    
    # pas de test pour __turn car c'est une méthode privée

    def test_turn_right(self):
        self.robot1.turn_right()
        self.assertEqual(self.robot1.__str__(), "R2-D2@(100,100) angle: 90.0")
        self.robot1.turn_left() # je remet le robot droit pour les autres tests

    def test_turn_left(self):
        self.robot1.turn_left()
        self.assertEqual(self.robot1.__str__(), "R2-D2@(100,100) angle: 270.0")
        self.robot1.turn_right() # je remet le robot droit pour les autres tests
    
    def test_history(self):
        self.robot1.move_forward(50)
        self.robot1.turn_left()
        self.assertEqual(self.robot1.history(), [("forward", 50),("left", 90)])
    
    def test_unplay(self):
        self.robot1.unplay()
        self.assertEqual(self.robot1.position(), (100,100))

if __name__ == '__main__':
    unittest.main(verbosity=2)