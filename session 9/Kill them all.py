class Character:
    def __init__(self, life, attack_point):
        self.life = life
        self.attack_point = attack_point
    def attack(self, target):
        target.get_hit(self.attack_point)
    def get_hit(self, damage):
        self.life -= damage
        
class Cratos(Character):
    def __init__(self):
        super().__init__(100, 10)
        self.experience = 0
        
    def gain_XP(self, amout):
        self.experience += amout
        while self.experience >= 10:
            self.experience -= 10
            self.attack_point += 1
      
class Drauf(Character):
    def __init__(self, life, attack_point):
        super().__init__(life, attack_point)