def create_index(list_of_words):
    """ Voir au dessus """
    d = {}
    ls = []
    for i in range(len(list_of_words)):
        if list_of_words[i] in d:
            d[list_of_words[i]].append(i)
        else:
            ls.append(i)
            d[list_of_words[i]] = ls
        ls = []
    return d