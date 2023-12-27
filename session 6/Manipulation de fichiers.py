def line_count(filename):
    """Cette fonction retourne le nombre de line dans le fichier donné."""
    file = open (filename, "r")
    counter = 0
    for line in file.readlines():
        counter +=1
    return counter
    file.close()

def char_count(filename):
    """ Cette fonction retourne le nombre de caractères dans un fichier donné. """
    file = open (filename, "r")
    caract = 0
    for line in file.readlines():
        for cara in line: 
            caract +=1
    return caract
    file.close()

def space(filename,n):
    """ Cette fonction retourne un nouveau fichier intitulé 'filename' composé de n espaces.
    """
    with open (filename, "w+") as file:
        file.write(" "*n)
        return filename
    
def capitalize(filename_in,filename_out):
    """ Cette fonction retourne le fichier 'filename_out' indentique à 'filename_in' sauf avec tout les charactères en majuscules.
    """
    try:
        with open (filename_in, "r") as f:
            with open (filename_out, "w") as out:
                for cara in f:
                    out.write(cara.upper())
    except:
        return "error"