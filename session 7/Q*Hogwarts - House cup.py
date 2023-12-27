def winning_house(scroll):
    resultat = {}
    with open(scroll,'r') as parchemin:
        for line in parchemin:
            data = line.strip().split(" ")
            for m in students:
                if data[0] in students[m]:
                    resultat[m] = resultat.get(m,0) + int(data[1])
    sorted_result = sorted(resultat,key=lambda k: resultat[k],reverse = True)
    n = 1
    while n < len(sorted_result) and resultat[sorted_result[n]] == resultat[sorted_result[n-1]]:
        n+=1
    if n == 1:
        return sorted_result[0]
    else:
        return sorted_result[:n]