def remove_from_end(self):
    if self.__length == 0:
        pass
    elif self.__length == 1:
        self.__head = None
        self.__length = 0
    else:
        pointer = self.first()
        while pointer.next().next() is not None:
            pointer = pointer.next()
        pointer.set_next(None)
        self.__length -= 1