# Seisdedos Stoz Diego
# BARB27 - Equipe 11.74

class OrderedLinkedList :
    
    def __init__(self, lst=[]):
        
        self.__length = 0     
        self.__head = None      
        self.__last = None        
        lst.reverse()            
        for e in lst :           
            self.add(e)
            
    def size(self):
        
        return self.__length
    
    def inc_size(self):
        
        self.__length += 1

    def dec_size(self):
        
        self.__length -= 1

    def first(self):
        
        return self.__head
    
    def set_first(self,n):
        
        self.__head = n
    
    def get_array(self): # nouvelle méthode

        node = self.first()
        r = []
        while node != None:
            r.append(node.value())
            node = node.next()
        return r
        
    def add(self, cargo): # méthode modifiée
        
        if self.first() == None:
            self.__add_to_begin(cargo)
        else:
            node = self.first()
            if cargo < self.first().value():
                self.__add_to_begin(cargo)
            elif cargo >= self.__last.value():
                self.add_to_end(cargo)
            else:
                while node is not None:
                    if node.next() is not None:
                        if node.value() <= cargo < node.next().value():
                            to_add = self.Node(cargo, node.next())
                            node.set_next(to_add)
                            self.inc_size()
                            break
                    node = node.next()

    def print(self):
        
        self.print_avec_separateur()

    def print_avec_separateur(self, separateur=" "):
        
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_list_avec_separateur(separateur)
        print("]")
        
    def print_avec_virgule(self):
        
        self.print_avec_separateur(", ")    
    
    def print_backward(self):
        
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_backward()
        print("]")

    def remove(self, cargo=None): # méthode modifiée

        if cargo == None:
            if self.first() is not None:
                self.dec_size()
                self.set_first(self.first().next())
            if self.size() == 0:      
                self.__last = None 
        else:
            node = self.first()
            previous = node
            while node != None:
                if node.value() == cargo:
                    if node == self.first():
                        self.remove()
                        return True
                    else:
                        previous.set_next(node.next())
                        self.dec_size()
                        return True
                previous = node
                node = node.next()
            return False

    def __add_to_begin(self, cargo): # nouvelle méthode

        if self.first() == None:
            node = self.Node(cargo, None)
            self.set_first(node)
            self.__last = node
        else:
            node = self.Node(cargo, self.first())
            self.set_first(node)
        self.inc_size()

    def add_to_end(self, cargo):
        
        if self.size() == 0 :       
            self.add(cargo)         
        else :                     
            node = self.Node(cargo)
            self.__last.set_next(node) 
            self.__last = node         
            self.inc_size()          

    def search(self, cargo): # nouvelle méthode

        node = self.first()
        i = 0
        while node is not None:
            if node.value() == cargo:
                return (node.value(), i)
            i+=1
            node = node.next()
        return None

    class Node:

        def __init__(self, cargo=None, next=None):
            
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            
            return self.__cargo

        def next(self):
            
            return self.__next

        def set_next(self,node):
            
            self.__next = node
    
        def __str__(self):
            
            return str(self.value())
    
        def __eq__(self,other):
            
            if other is not None :
                return self.value() == other.value()
            else :
                return False

        def print_list(self):
            
            head = self
            tail = self.__next       
            if tail is not None :  
                print(head, end=" ")  
                tail.print_list()    
            else :                   
                print(head, end=" ")

        def print_backward(self):
            
            head = self
            tail = self.__next   
            if tail is not None :    
                tail.print_backward() 
            print(head, end = " ")    

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self,separateur):
            head = self
            tail = self.__next 
            if tail is not None : 
                print(head, end=separateur) 
                tail.print_list_avec_separateur(separateur) 
            else:              
                print(head, end=" ") 

if __name__ == "__main__":
    lst = OrderedLinkedList([11,44,55,12])
    lst.print()
    lst.add(77)
    lst.print()
    lst.remove(44)
    lst.print()
    print(lst.search(11))
    print(lst.get_array())