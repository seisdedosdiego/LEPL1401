def create_dict(l):
    """ Voir au dessus """
    d = {}
    ls = []
    for i in l:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            ls.append(i[1])
            d[i[0]] = ls
        ls = []
    return d