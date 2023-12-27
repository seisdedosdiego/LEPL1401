child = first_child
while child.next_child() != first_child:
    if child.is_next_valid() == False:
        return False
    else:
        child = child.next_child()
return True