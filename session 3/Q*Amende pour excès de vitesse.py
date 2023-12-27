def fine(authorized_speed, actual_speed):
    """Cette fonction calcule l'amende d'un excès de vitesse.
       pré: authorized_speed et actual_speed 2 nombres entiers positifs
       post: retourne le montant de l'amende
    """
    if authorized_speed >= actual_speed:
        return 0
    elif (authorized_speed - actual_speed > -2.5):
        return 12.5
    elif (authorized_speed - actual_speed < -2.5) and (authorized_speed - actual_speed > -10):
        x = actual_speed - authorized_speed
        y = abs(x)
        return y*5
    elif (authorized_speed - actual_speed <= -10):
        x = actual_speed - authorized_speed
        y = abs(x)
        return y*5*2