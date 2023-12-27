if b==0:
    rest = None
else:
    while a>=b:
        a=a-b
    rest = a
    print(rest)