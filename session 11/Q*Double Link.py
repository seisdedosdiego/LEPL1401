class Tape:
    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__point = None
        self.__last = None
    def next(self):
        if self.__point != self.__last:
            self.__point = self.__point.next
            return self.__point.get_text()
        else: 
            return None
    def previous(self):
        if self.__point != self.__head:
            self.__point = self.__point.previous
            return self.__point.get_text()
        else:
            return None
    def get_length(self):
        return self.__length
    def add(self,s):
        if self.__length == 0:
            node = Node(s, None, None)
            self.__head = node
            self.__last = node
            self.__point = node
        else:
            old = self.__last
            self.__last = Node(s, old, None)
            old.next = self.__last
        self.__length += 1
    def write(self, s):
        if self.__point is not None:
            self.__point.set_text(s)
    def read(self):
        if self.__point != None:
            return self.__point.get_text()
        else: 
            return None