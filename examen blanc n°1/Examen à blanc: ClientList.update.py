node = self.last
while node is not None:
    if node.data.getUserName() == name:
        node.data.setPin(pin)
        return
    node = node.link
self.last = self.Node(Client(name,pin),self.last)

# ZONE TEST #
cl = ClientList()
cl.update("alice", 1234)
cl.update("benoit", 2345)
cl.update("alice", 3333)
print(cl)