# Ne faites pas ça, il y a beaucoup plus simple et moins long...

def extract(code):
    """ Cette fonction analyse chaque caractère dans le code donné et détermine sa nature.
        pré: code une chaîne de caractère
        post: retourne une chaîne de caractère
    """
    code_exit = ""
    for i in code:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
            code_exit += "vowel-low "
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
            code_exit += "vowel-up "
        elif i == "b" or i == "c" or i == "d" or i == "f" or i == "g" or i == "h" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "v" or i == "w" or i == "x" or i == "z":
            code_exit += "consonant-low "
        elif i == "B" or i == "C" or i == "D" or i == "F" or i == "G" or i == "H" or i == "J" or i == "K" or i == "L" or i == "M" or i == "N" or i == "P" or i == "Q" or i == "R" or i == "S" or i == "T" or i == "V" or i == "W" or i == "X" or i == "Z":
            code_exit += "consonant-up "
        else: 
            code_exit += "number "
        
    code_exit = code_exit[:-1]
            
    return code_exit