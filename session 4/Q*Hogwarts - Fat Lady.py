def portrait(right_password, entered_password):
    """ Cette fonction retourne 'True' si les deux mots de passe sont identiques et 'False' sinon.
        pré: right_password et entered_password des chaînes de caractères.
        post: retourne 'True' ou 'False'
    """
    if right_password == entered_password:
        return True
    else: 
        return False