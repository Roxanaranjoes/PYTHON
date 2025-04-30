#años para jubilarse
edad=int(input("Ingrese su edad: "))
genero=(input("Ingrese su genero: ")) .lower()
añosfaltantesmujer = 60-edad
añosfaltanteshombre= 65-edad


if genero=="mujer" and edad>=60:
    print("Felicidades!Puede usted jubilarse") 
    
elif genero== "mujer" and edad<=60:
    print(f"A usted le faltan {añosfaltantesmujer} años para jubilarse")


else:
    if genero== "hombre" and edad>=65:
        print("Felicidades!Puede usted jubilarse")
    elif genero== "hombre" and edad<=65:
        print(f"A usted le faltan {añosfaltanteshombre} años para jubilarse")
        

    


