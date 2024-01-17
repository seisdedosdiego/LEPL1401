def extract(code):
    res = ""
    upper_caract_cons = "ZRTPQSDFGHJKLMWXCVBN"
    lower_caract_cons = "zrtpqsdfghjklmwxcvbn"
    upper_caract_voy = "AEYUIO"
    lower_caract_voy = "aeyuio"
    for i in code:
        if i in upper_caract_cons:
            res += "consonant-up "
        elif i in upper_caract_voy:
            res += "vowel-up "
        elif i in lower_caract_cons:
            res += "consonant-low "
        elif i in lower_caract_voy:
            res += "vowel-low "
        else:
            res += "number " 
    res = res.strip()
    return res
