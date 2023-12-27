from graphics import GraphWin, Line, Point 
from math import pi, cos, sin            
import time
from Robot import Robot as rob

class XYRobot(rob):
    
    def __init__(self,nom,x=0,y=0) :
        super().__init__(nom)
        self.__x = x               
        self.__y = y               
        self.__angle = 0           
        self.__win = GraphWin()

    def x(self) :
        return self.__x
    
    def y(self) :
        return self.__y
    
    def angle_rad(self) :
        "retourne l'angle en degres radius représentant la direction du robot"    
        return self.__angle

    def angle(self) :
        "retourne l'angle en degres représentant la direction du robot"    
        return ( self.angle_rad() * 180 / pi ) % 360
        
    def __set_x(self,x) :
        self.__x = x
        
    def __set_y(self,y) :
        self.__y = y

    def __set_angle_rad(self,angle) :
        self.__angle = angle

    def position(self) :
        return (self.x(),self.y())

    def __draw_from(self,old_x,old_y) :
        """
        méthode auxiliaire pour tracer une ligne de l'ancienne position
        (old_x,old_y) du robot à sa position (x,y) actuelle
        """        
        line = Line(Point(old_x,old_y),Point(self.x(),self.y()))
        line.draw(self.__win)
        
    def __move(self,distance,sense) :
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  fait avancer le robot de distance pixels
            si sense = -1 fait reculer le robot de distance pixels
        """
        old_x = self.x()
        old_y = self.y()
        orientation_x = cos(self.angle_rad())
        orientation_y = sin(self.angle_rad())
        self.__set_x(old_x + orientation_x * distance * sense)
        self.__set_y(old_y + orientation_y * distance * sense)
        self.__draw_from(old_x,old_y)

    def move_forward(self,distance) :
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance,1)
        super().move_forward(distance)

    def move_backward(self,distance) :
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance,-1)
        super().move_backward(distance)

    def __turn(self,direction) :
        """ méthode auxiliaire pour les méthodes turn_right() et turn_left()
            si direction = 1 change l'angle du robot de 90 degrés vers la droite
                             (dans le sens des aiguilles d'une montre)
            si direction = -1 change l'angle du robot de 90 degrés vers la gauche
                             (dans le sens contraire des aiguilles d'une montre)
        """
        self.__set_angle_rad(self.angle_rad() + direction * pi/2)
        
    def turn_right(self) :
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(1)
        super().turn_right()

    def turn_left(self) :
        """ fait tourner le robot de 90 degrés vers la gauche
            (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-1)
        super().turn_left()
    
    def unplay(self):
        history = self.history()
        for i in range(len(history)-1, -1, -1):
            if history[i][0] == "forward":
                self.__move(history[i][1], -1)
            elif history[i][0] == "backward":
                self.__move(history[i][1], 1)
            elif history[i][0] == "right":
                self.__turn(-1)
            elif history[i][0] == "left":
                self.__turn(1)
        self.clear_history()
    
if __name__ == '__main__':
    r2d2 = XYRobot("R2-D2",100,100)

    print(r2d2)

    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    
    r2d2.move_forward(50)
    print(r2d2)
    
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)

    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)

    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)

    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)

    r2d2.unplay()
    print(r2d2.history())

    time.sleep(3)