def table(filename_in, filename_out, width):
    """ Cette fonction retourne un fichier 'filename_out' qui avec les éléments du fichier 'filename_in' dans un encadré de           largeur 'width' tel le dessin au dessus.
        pré: 'filename_in' un fichier, 'filename_out' un str et 'width' in int 
        post: retourne un fichier 'filename_out' qui contient un tableau comme celui demandé 
    """
    file_in = open (filename_in, "r").readlines()
    file_out = open (filename_out, "w") 
    
    
    file_out.write("+")
    for i in range(width+2):
        file_out.write("-")
    file_out.write("+" + "\n")
    
    for line in file_in:
        if len(line)-1 > width:
            new_line = line.rstrip()
            diff = len(new_line)-width
            new_line2 = new_line[:-diff]
            file_out.write("| " + new_line2 + " |" + "\n")
        elif len(line)-1 == width:
            new_line = line.rstrip()
            file_out.write("| " + new_line + " |" + "\n")
        else:
            new_line = line.rstrip()
            diff = width-len(new_line)
            file_out.write("| " + new_line + " "*diff +" |" + "\n")
    
    file_out.write("+")
    for i in range(width+2):
        file_out.write("-")
    file_out.write("+")
    
    return file_out