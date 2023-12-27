def get_country(l,name):
    """ Voir au dessus (flemme) """
    for i in range(len(l)):
        d = {}
        d = l[i]
        if d["City"] == name:
            return d["Country"]
    return False