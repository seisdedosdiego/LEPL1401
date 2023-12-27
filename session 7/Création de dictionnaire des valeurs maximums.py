def create_dict_max(l):
    """ Voir au dessus """
    d = {}
    for i in l:
        if i[0] in d:
            if d[i[0]] < i[1]:
                d[i[0]] = i[1]
        else:
            d[i[0]] = i[1]
    return d