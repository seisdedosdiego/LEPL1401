class Node:
    def __init__(self,cargo,next=None):
        self.__cargo = cargo
        self.__next = next
    def get_value(self):
        return self.__cargo
    def get_next(self):
        return self.__next
    def __str__(self):
        return str(self.get_value())
        
class LinkedList:
    def __init__(self):
        self.__length = 0
        self.__head = None
    def add(self, val):
        node = Node(val,self.__head)
        self.__head = node
        self.__length += 1
    def get_reverse(self):
        head = self.__head
        x = ""
        for _ in range(self.__length):
            x += str(head)
            head = head.get_next()
        return x