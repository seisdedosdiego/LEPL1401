solutions = 0
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x, y et z : "))

for x in range(1,max):
    for y in range(1,max):
        for z in range(1, max):
            if x**a + y**b == z**c and (x%y!=0 or y%x!=0) and (x%z!=0 or z%y!=0) and (y%z!=0 or z%y!=0):
                print("x =", x, " y =", y, "z =",z)
                solutions += 1



if solutions == 0:
    print("Aucune solution trouvée")
elif solutions == 1:
    print (solutions, "solution trouvée")
else:
    print(solutions, "solutions trouvées")

    
