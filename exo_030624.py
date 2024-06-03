#Exercice 2:

#Si le nombre saisi est inférieur à n, afficher "trop petit", puis répéter
while True:
    n = 12 #Nombre à deviner
    nombre = int(input("Deviner un nombre : "))
    if nombre < n:
        print(nombre, "est trop petit, veulliez répéter")
    elif nombre > n :
        print(nombre, "est trop grand, veulliez répéter")
        
    if nombre == n:
        print("bravoo!!! vous avez trouvé, le nombre que vous chercher est bien", n)
        break
