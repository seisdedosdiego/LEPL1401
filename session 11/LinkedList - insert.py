def insert(self, s):
    after = self.__head
    if after == None:
        self.__head = Node(s,after)
    elif s < after.value():
        self.__head = Node(s,after)
    else:
        for i in range(self.size()-1):
            before = after
            after = before.next()
            if after == None:
                before.set_next(Node(s))
                break
            elif s < after.value():
                before.set_next(Node(s,after))
                break
            else:
                before = after
                after = before.next()