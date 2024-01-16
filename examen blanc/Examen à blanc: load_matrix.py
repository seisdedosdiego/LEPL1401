try:
    with open (filename, "r") as f:
        list = []
        for line in f:
            new_line = line.rstrip()
            list.append(new_line)

        matrix_num_line = int(list[0])
        matrix_num_colo = int(list[1])
        matrix = []
        for i in range(0,matrix_num_line):
            matrix.append([])
            for j in range(0,matrix_num_colo):
                matrix[i].append(0.0)       

        for i in range(2,len(list)):
            info = list[i].split(" ")
            #print(info)
            info_position = info[0].split(",")
            #print(info_position)
            matrix[int(info_position[0])][int(info_position[1])] = info[1]
        return matrix
except: 
    return None