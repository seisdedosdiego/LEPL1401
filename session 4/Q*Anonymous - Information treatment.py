def treatment(data):
    res = ""
    ls = data.split()
    prev = ls[0]
    count = 1
    for i in range(1,len(ls)):
        if ls[i] == prev:
            count +=1
        else:
            res += str(ls[i-1]) + "*" + str(count) + " "
            prev = ls[i]
            count = 1
    res += str(ls[-1]) + "*" + str(count)
    return res
