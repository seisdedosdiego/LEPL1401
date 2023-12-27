class Weapon:
    def __init__(self, attack):
        """ Spécifications """
        self.attack = attack

class Cratos:
    def __init__(self, weapon):
        """ Spécifications """
        self.weapon = weapon
    def set_weapon(self, weapon):
        """ Spécifications """
        self.weapon = weapon
    def hit(self, enemy):
        """ Spécifications """
        damage = self.weapon.attack
        enemy.get_hit(damage)
        
class Drauf:
    def __init__(self, life):
        """ Spécifications """
        self.life = life
    def get_hit(self, damage):
        """ Spécifications """
        self.life -= damage