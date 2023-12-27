class Animal:
    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False
        
    def sleep(self):
        if self.asleep == True:
            raise RuntimeError
        self.asleep = True
        
    def wake_up(self):
        if self.asleep == False:
            raise RuntimeError
        self.asleep = False

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        
    def roar(self):
        print("ROARRR!!!")
        
class Owl(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = False
        self.nb_legs = 2
        
    def fly(self):
        pass

class Giraffe(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        if (type(length) == int or type(length) == float) and length > 0:
            self.neck_length = length
        else:
            raise ValueError ("Error")

class Zoo:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        if isinstance(animal,Animal) == False:
            raise ValueError ("Error")
        else:
            self.animals.append(animal)
            
def create_my_zoo():
    zoo = Zoo()
    zoo.add_animal(Lion("name1"))
    zoo.add_animal(Owl("name2"))
    zoo.add_animal(Giraffe("name3", 1))
    zoo.add_animal(Giraffe("name4", 2.5))
    return zoo

create_my_zoo()