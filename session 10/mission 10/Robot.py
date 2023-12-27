# Seisdedos Stoz Diego 
# BARB27 - Equipe 11.74

import math

class Robot:
    def __init__(self, nom):
        self.__nom = nom
        self.__history = []
    
    def __str__(self):
        return str(self.nom()) + "@(" + str(round(self.x())) + "," + \
               str(round(self.y())) +") angle: "+str(self.angle())
    
    def nom(self):
        return self.__nom
    
    def move_forward(self,distance):
        self.__history.append(("forward",distance))

    def move_backward(self,distance):
        self.__history.append(("backward",distance))

    def turn_right(self):
        self.__history.append(("right",90))

    def turn_left(self):
        self.__history.append(("left",90))

    def history(self):
        return self.__history

    def clear_history(self):
        self.__history = []
        