def write(letter_template, name):    
    """ Cette fonction remplace le contenu du fichier 'letter_template' par le même texte 
        en remplaçant le caractère '#' par le nom de l'étudiant 'name'.
    """
    try:
        with open(letter_template, "r") as file:
            letter = file.read()
        with open(letter_template,"w") as file:
            for i,j in enumerate(letter):
                if j == "#":
                    letter = letter[:i] + name + letter[i+1:]
            file.write(letter)
        
    except OSError:
        raise OSError("erreur")