def referee(score_file):
    """ Cette fonction retourne l'équipe gagnant du match de Quidditch. """
    
    try : 
        with open(score_file, "r") as f:
        
            sum_team1 = 0
            sum_team2 = 0
            line1 = f.readline()
            line2 = f.readline()
            name_team1 = line1.rstrip()
            name_team2 = line2.rstrip()
            for line in f:
                new_line = line.rstrip()
                word_list = new_line.split(" ")
                if word_list[0] == name_team1:
                    if int(word_list[1]) == 150:
                        return name_team1
                    else:
                        sum_team1 += int(word_list[1])
                if word_list[0] == name_team2:
                    if int(word_list[1]) == 150:
                        return name_team2
                    else:
                        sum_team2 += int(word_list[1])
            if sum_team1 > sum_team2:
                return name_team1
            elif sum_team1 < sum_team2:
                return name_team2
            elif sum_team1 == sum_team2:
                return "Draw"
    except OSError:
        raise OSError ("An error occured")