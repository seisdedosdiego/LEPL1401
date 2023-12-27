def write_coordinates(filename, l):
    """ Cette fonction retourne un fichier 'filename' à partir de données d'une liste 'l'.
    """
    try: 
        with open(filename, "w") as file:
            rep = ""
            for i in l:
                rep += str(i[0]) + "," + str(i[1]) + "\n"
            file.write(rep[:-1])
            return file
    except:
        return "error"
    
def read_coordinates(filename):
    """ Cette fonction retourne une liste de tuples avec les coordonnées du fichier 'filename'.
    """
    try:
        with open(filename, "r") as file:
            list = [] 
            for line in file.readlines():
                x,y = line.split(",")
                list.append((float(x), float(y)))
            return list
    except:
        return "error"