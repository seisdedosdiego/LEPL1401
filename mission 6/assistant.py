# Diego Seisdedos Stoz
# BARB27

# BODY OF THE PROGRAM

def command():
    """ Cette fonction demande à l'utilisateur une commande.
        pré : rien
        post : retourne la commande de l'utilisateur
    """
    command = input("Entrez une commande > ")
    return command

def file(name):
    """ Cette fonction défini le fichier 'name' comme l'outil de travail à partir de maintenant.
        pré: 'name' un string
        post: indique sur quel ficher l'utilisateur se trouve
    """
    print("Le fichier '" + name + "'est chargé")
    
def info(name):
    """ Cette fonction retourne le nombre de lignes et caractères du fichier chargé.
        pré: le nom du fichier chargé
        post: le nombre de lignes et caractères
    """
    with open(name, "r") as file:
    
        line = 0
        caract = 0
    
        for i in file:
            line += 1
            for j in i:
                caract += 1
    
        print("Le fichier contient :" + "\n" + str(line) + " lignes" + "\n" + str(caract) + " caractères")
        
    file.close()

def words(name):
    """ Cette fonction transforme le fichier en liste de mots.
        pré: le nom du fichier
        post: retourne une liste avec les mots
    """
    ls = []
    
    with open (name, "r") as file:
        
        for line in file:
            ln = line.split()
            for i in ln:
                ls.append(i)
    return ls
            
            
        
    
def search(word, file):
    """ Cette fonction vérifie si le mot est compris dans la liste de mots (provenant du fichier).
        pré: un mot et un nom de fichier
        post: retourne si le mot est dans la liste ou pas
    """
    ls = words(file)
    found = False
    for i in ls:
        if i == word:
            found = True
    
    if found:
        print("Le mot est dans la liste")
    else:
        print("Le mot n'est pas dans la liste")
        
    
def sum(n1,n2):
    """ Cette fonction retourne la somme de 2 nombres.
        pré: 2 nombres
        post: leurs sommes
    """
    sum = float(n1) + float(n2)
    print ("La somme de " + str(n1) + " et " + str(n2) + " est " + str(sum))
    
def avg(n1,n2):
    """ Cette fonction retourne la moyenne entre 2 nombres.
        pré: 2 nombres
        post: leurs moyenne
    """
    avg = (float(n1)+float(n2))/2
    print("La moyenne de " + str(n1) + " et " + str(n2) + " est " + str(avg))
    
def help():
    """ Cette fonction montre les instructions à l'utilisateurs """
    print("Liste des commandes possibles : " + "\n" + "1. file <name> : ouvre le fichier 'name'" + "\n" +  "2. info <name> : donne des caractéristiques sur le fichier 'name'" + "\n" +
          "3. words <name> : retourne une liste avec tous les mots du fichier 'name'" + "\n" "4. search <word> <name> : recherche si le mot 'word' fait partie de la liste de mots de 'name'" + "\n" +
          "5. sum <n1> <n2> : retourne la somme des 2 nombres" + "\n" + "6. avg <n1> <n2> : retourne la moyenne des 2 nombres" + "\n" + "7. help : retourne des infos sur les commandes possibles" + "\n" +
          "8. exit : quitte le programme" + "\n" + "9. ***** : commande secrete")
   
def exit():
    """ Cette fonction arrête le programme.
        pré: rien
        post: arrête le programme
    """
    print("Arrêt du programme...")
    
# HEAD OF THE PROGRAM

def program():
    """ Cette fonction est chargé de faire fonctionner le programme.
        pré: rien
        post: le programme qui fonctionne
    """
    
    com = command()
    com_lst = com.split(" ")
    
    try : 
        if com_lst[0] == "exit":
            exit()
        
        elif com_lst[0] == "file":
            file(com_lst[1])
            program()
    
        elif com_lst[0] == "info":
            info(com_lst[1])
            program()
        
        elif com_lst[0] == "words":
            print(words(com_lst[1]))
            program()
    
        elif com_lst[0] == "search":
            search(com_lst[1], com_lst[2])
            program()
        
        elif com_lst[0] == "sum":
            sum(com_lst[1], com_lst[2])
            program()
    
        elif com_lst[0] == "avg":
            avg(com_lst[1], com_lst[2])
            program()
    
        elif com_lst[0] == "help":
            help()
            program()
        elif com_lst[0] == "*****":
            print("Abracadabra")
            program()
        else:
            raise error
         
    except:
        print("Commande non reconnue")
        program()
        
program()
    