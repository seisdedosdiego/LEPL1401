def translate(data, lan):
    """ Voir au dessus """
    new_data1 = data.lower()
    new_data2 = new_data1.strip().split(" ")
    translation = ""
    for i in new_data2:
        if i in lan:
            translation += lan[i]
            translation += " "
        else:
            translation += i
            translation += " "
    translation1 = translation.rstrip()
    return translation1