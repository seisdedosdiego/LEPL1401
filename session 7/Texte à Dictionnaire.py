def create_dictionary(filename):
    """ Voir au dessus (flemme) """
    dictionary = {}
    with open (filename, "r") as f:
        for line in f:
            list_words = []
            new_line = line.rstrip()
            list_words = new_line.split(" ")
            for i in list_words:
                if i in dictionary:
                    dictionary[i] += 1
                else:
                    dictionary[i] = 1
    return dictionary
            
def occ(dictionary, word):
    """ Voir au dessus (flemme) """
    if word in dictionary:
        return dictionary[word]
    else: 
        return 0