def marks_from_file(filename):
    """ Spécification """
    list = []
    with open (filename, "r") as f:
        for line in f:
            l = line.strip().split(" ")
            list.append(Student(l[0], l[1], int(l[2])))
    return list