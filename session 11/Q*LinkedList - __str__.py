def __str__(self):
    string = "[ "
    pointer = self.first()
    while pointer != None:
        string += str(pointer)+" "
        pointer = pointer.next()
    string += "]"
    return string