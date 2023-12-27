def __str__(self):
    return str(self.r1) + " | " + str(self.r2)

def moveforward(self, distance):
    super().moveforward(distance)
    self.r1.moveforward(distance)
    self.r2.movebackward(distance)
    
def movebackward(self, distance):
    super().movebackward(distance)
    self.r1.movebackward(distance)
    self.r2.moveforward(distance)
    
def turnright(self):
    super().turnright()
    self.r1.turnright()
    self.r2.turnleft()
    
def turnleft(self):
    super().turnleft()
    self.r1.turnleft()
    self.r2.turnright()
    
def unplay(self):
    self.r1.unplay()
    self.r2.unplay()
    self.clearHistory()