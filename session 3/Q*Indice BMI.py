def quetelet(height, weight):
    if (weight/height**2)<20:
        return "thin"
    elif (weight/height**2)>=20 and (weight/height**2)<=25:
        return "normal"
    elif (weight/height**2)>25 and (weight/height**2)<=30:
        return "overweight"
    else:
        return "obese"