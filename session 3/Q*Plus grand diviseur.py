if a == 0 or a == 1: 
    return None
else:
    for i in range(a-1,0,-1):
        if a%i==0:
            return i