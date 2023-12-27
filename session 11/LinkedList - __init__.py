def __init__(self, lst):
    """ 
        Cette méthode prend une list en argument et initialise une liste chaînée dans le même ordre que la liste.
        pré: lst une liste
        post: une liste chaînée avec pour premier élément le premier élément de la liste lst
    """
    self.__length = len(lst)
    self.__head = None
    
    for i in range(len(lst)-1, -1, -1):
        node = Node(lst[i], self.__head)
        self.__head = node