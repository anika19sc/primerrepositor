#Escribir un programa que permita ingresar las edades de las personas, hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas. 
persona=0 #Es un contador.
bool=1 #Es un booleano.
edad=0 #Es un acumulador.
while bool==1:
 edades=int(input("Ingrese edad")) 
 persona+=1
 edad=edad+edades
 promedio=edad/persona
 bool=int(input("Desea seguir coloque: 1(Si) o 0(No)")) #Preguntamosa al usuario si desea seguir con el programa.
 if bool==0: #Si el usuario pone 0 no se ejecutara mas el programa.
      print("El promedio de edad es" ,promedio)
      print("El total de personas ingresadas" ,persona)
 elif bool > 1: #Si el usuario coloca otro numero mayor a uno, el programa avisara que es error.
     print("Numero incorrecto")
 
 