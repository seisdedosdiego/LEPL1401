command = input ( "Enter your command: " )
parameters = command.split ()
if parameters[0] == "divide":
    print ( "The value of your division is: " + str ( float(parameters[1])/float(parameters[2])))
elif parameters[0] == "showfile":
    file = open ( parameters[1] )
    print ( file.read () )
    file.close ()
else:
    print ( "Command not recognized")