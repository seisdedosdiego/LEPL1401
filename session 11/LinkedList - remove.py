def remove(self):
    if self.__head == None:
        pass
    else:
        self.__head = self.__head.next()
        self.__length -= 1