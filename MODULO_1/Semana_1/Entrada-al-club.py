#Entrada al club unicornio ninja 
edad=int (input ("Ingresa tú edad: "))
pase=input ("¿Tienes pase dorado? si/no: "). lower ()

if edad<18:
 print("No puedes entrar al Club Unicornio Ninja")
elif pase == "si" and edad>18:
 print( "Puedes entrar al Club Unicornio Ninja")

else:
 if edad<=25:
  print("Puedes entrar al Club Unicornio Ninja")
 else:
     print("No puedes entrar al Club Unicornio Ninja ")