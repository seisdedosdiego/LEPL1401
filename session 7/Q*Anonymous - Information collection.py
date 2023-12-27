def collect(file):
    lines = open (file, "r").readlines()
    lines = [treatment(extract(line.strip())) for line in lines]
    occ = {}
    for l in lines:
        is_in = False
        for o in occ:
            if l == o:
                occ[o] += 1
                is_in = True
                break
        if not is_in:
            occ[l] = 1
    return occ