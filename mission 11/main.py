# Seisdedos Stoz Diego
# BARB27 - Equipe 11.74

import random
import time
from coureur    import Coureur
from classement import Classement
from temps      import Temps
from resultat   import Resultat

class Main :
   
    coureurs = [ Coureur("Alfred", 24), \
                 Coureur("Bernard", 27), \
                 Coureur("Claude", 19), \
                 Coureur("Daniel", 31),  \
                 Coureur("Emile", 25),  \
                 Coureur("Fred", 28),  \
                 Coureur("Gerard", 25) ]

    @classmethod
    def main(cls) :
        
        cl = Classement()      
        while True :                 
            c = random.choice(cls.coureurs)            
            t = Temps()
            t.add_secondes(random.randint(1000, 5000))            
            r = Resultat(c, t)
            print(r)           
            r1 = cl.get(r.coureur())            
            if r1 is None :
                print("  Pas encore classé")
            else:
                print("  Actuellement classé " + str(cl.get_position(c)))
                print("  Dernier temps enregistré = " + str(r1.temps()))            
            if r1 is not None and r >= r1 :
                print("  Moins bon temps, ignoré")
            else :
                print("  Nouveau temps est meilleur; sera enregistré")
                cl.remove(c)
                cl.add(r)
                print("  Maintenant classé " + str(cl.get_position(c)));
                print()
                print("CLASSEMENT:")
                print(cl)
                print() 
            time.sleep(1)

Main.main()