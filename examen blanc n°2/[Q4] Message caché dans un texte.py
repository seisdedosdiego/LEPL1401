def acrostiche(file_name): # Ne pas effacer cette ligne
    """
    @pre:  file_name est le nom d'un fichier de texte
    @post: Retourne une chaîne de caractères contenant la première lettre
          de chaque ligne dans le fichier de texte,
          pour les lignes qui contiennent au moins un caractère.
          Retourne -1 en cas d'erreur d'accès au fichier.
    """
    try:
        with open (file_name, "r") as f:
            word = ""
            for line in f:
                for cara in line:
                    if cara.isalpha():
                        word += cara
                        break
        return word
    except:
        return -1  
    
# ZONE TEST #
create_file(["","Elizabeth it is in vain you say.","'Love not'-thou sayest it in so sweet a way:","In vain those words from thee or L.E.L.","Zantippe's talents had enforced so well:","Ah! if that language from thy heart arise,","Breath it less gently forth-and veil thine eyes.","Endymion, recollect, when Luna tried","To cure his love-was cured of all beside-","His follie-pride-and passion-for he died.",""])

def test_acrostiche():
    assert acrostiche("test.txt") == "ELIZABETH", "test 1"
    print("TOUT OK")
    
test_acrostiche()