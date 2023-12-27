# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74

def readfile(filename):
    """ Voir consignes """
    try:
        list = []
        with open (filename, "r") as f:
            for line in f:
                new_line = line.rstrip()
                list.append(new_line)
            return list
    except:
        return "An error occured"

def get_words(line):
    """ Voir consignes """
    list0 = line.split(" ")
    list1 = []
    list2 = []
    for i in list0:
        list1.append(i.lower())
    for j in list1:
        new_str = ""
        for k in j:
            if k.isalpha():
                new_str += k
        if new_str != "":
            list2.append(new_str)
    return list2
    
def create_index(filename):
    """ Voir consignes """
    try:
        with open (filename, "r") as f:
            list_of_lines = readfile(filename)
            list_of_words = []
            dict = {}
            counter = -1
        
            for i in list_of_lines:
                counter +=1
                list_of_words = get_words(i)
            
                for j in list_of_words:
                    list_line = []
                    if j in dict:
                        dict[j].append(counter)
                    else:
                        list_line.append(counter)
                        dict[j] = list_line
                    
            for i in dict:
                ls = dict[i]
                ls1 = list(set(ls))
                dict[i] = ls1

            return dict
    except:
        return "An error occured"
        
def get_lines(words,index):
    """ Voir consignes """
    try: 
        stock = []
        new_stock = []
        for i in words:
            if i in index:
                stock.append(index[i])
        if stock == []:
            return stock
        
        stock1 = stock
        
        for j in range(len(stock1)-1):
            stock2 = []
            x = stock1[0]
            y = stock1[1]
            for k in x:
                for l in y:
                    if k == l:
                        stock2.append(k)
            stock1[1] = stock2
            del(stock1[0])
            
        stock3 = stock1[0]
        stock4 = list(set(stock3))
        return stock4
    except:
        return "Error"
        
    
