def save_data(filename, life, mana, position_x, position_y):
    """ Sauvegarder les 4 entiers dans le fichier nommé 'filename'. """
    with open (filename, "w") as f:
        f.write(str(life)+ "\n")
        f.write(str(mana)+ "\n")
        f.write(str(position_x) + "\n")
        f.write(str(position_y) + "\n")
        
def load_data(filename):
    """ Retourne un tuple contenant les valeurs (life, mana, position_x et position_y précédemment sauvegardées. """
    try: 
        with open (filename, "r") as f:
            ls = []
            for line in f:
                l = line.rstrip()
                l1 = int(l)
                ls.append(l1)
            my_tuple = tuple(ls)
            return my_tuple
        
    except FileNotFoundError: 
         raise FileNotFoundError("File Error")