def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_max(filename):
    z = -1
    try: 
        with open(filename, "r") as f:
            x = 0
            for line in f:
                line_1 = line.rstrip()
                line_ls = line_1.split(" ")
                if len(line_ls) > 1:
                    pass
                else:
                    found = isNumeric(line_ls[0])
                    if found == True:
                        y = float(line_ls[0])
                        if y > x:
                            x = y
            if x > 0:
                return x
            else:
                return z
    except FileNotFoundError:
        print("Error")
        return z