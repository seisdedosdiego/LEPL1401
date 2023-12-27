def translate(data):
    """ Voir au dessus """
    try:
        l = data.upper()
        data1 = l.split()
        new_data = ""
        for i in data1:
            for j in i:
                if j in morse:
                    new_data += morse[j]
                else:
                    raise ValueError ("Error")
        return new_data
    
    except ValueError: 
        raise ValueError ("Error")