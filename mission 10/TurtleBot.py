# Seisdedos Stoz Diego 
# BARB27 - Equipe 11.74

import turtle
import math
import time
from Robot import Robot as rob

class TurtleBot(rob):
    def __init__(self, nom, x=0, y=0):
        super().__init__(nom)
        self.__x = x
        self.__y = y
        self.__angle = 0.0
        self.t = turtle.Turtle()
        #self.t.hideturtle()

    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def angle_rad(self):
        return self.__angle
    
    def angle(self):  
        return (self.angle_rad()*180/math.pi)%360
    
    def __set_x(self,x=x):
        self.__x = x

    def __set_y(self,y=y):
        self.__y = y

    def __set_angle_rad(self,angle=angle):
        self.__angle = angle
    
    def position(self):
        return (self.x(),self.y())
    
    def __move(self,distance,sense):
        if sense == 1:
            self.t.penup()
            self.t.goto(self.position()[0],self.position()[1])
            self.t.pendown()
            self.t.forward(distance)
            self.__set_x(x=self.t.pos()[0])
            self.__set_y(y=self.t.pos()[1])
        elif sense == -1:
            self.t.penup()
            self.t.goto(self.position()[0],self.position()[1])
            self.t.pendown()
            self.t.forward(-distance)
            self.__set_x(x=self.t.pos()[0])
            self.__set_y(y=self.t.pos()[1])

    def move_forward(self,distance):
        self.__move(distance, 1)
        super().move_forward(distance)

    def move_backward(self,distance):
        self.__move(distance, -1)
        super().move_backward(distance)

    def __turn(self, direction):
        if direction == 1:
            self.t.right(90)
            self.__angle = math.pi*self.t.heading()/180
        elif direction == -1:
            self.t.left(90)
            self.__angle = math.pi*self.t.heading()/180

    def turn_right(self):
        self.__turn(1)
        super().turn_right()

    def turn_left(self):
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

    # test pour voir ce que ça donne
    bot = TurtleBot("R2-D2")

    print(bot)

    bot.move_forward(50)
    bot.turn_left()
    print(bot)

    bot.move_forward(50)
    bot.turn_left()
    print(bot)

    bot.move_forward(50)
    bot.turn_left()
    print(bot)

    bot.move_forward(50)
    print(bot)

    bot.move_forward(50)
    bot.turn_right()
    print(bot)

    bot.move_forward(50)
    bot.turn_right()
    print(bot)

    bot.move_forward(50)
    bot.turn_right()
    print(bot)
    
    bot.move_forward(50)
    print(bot)

    bot.unplay()
    print(bot.history())
    
    time.sleep(5)


    


    