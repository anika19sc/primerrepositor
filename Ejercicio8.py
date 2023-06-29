"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""
contador = 1
#En este ejercicio utilizaremos un "while" que al usuario va a permitirle ingresar o ejecutar varias veces al programa.
while contador <= 5: #El programa va a permitir que 5 personas ingresen.
    print("Persona nº", contador) #Cuenta la personas que ingresaron.
    nombre = str(input("Ingrese un nombre: ")) #Ingresar dato.
    apellido = str(input("Ingrese un apellido: ")) #Ingresar dato.
    edad = int(input("Ingrese edad: ")) #Ingresar dato. 

    print("*Sus datos son los siguientes:")
    #Lo siguiente que va a pasar es mostrar los nombres, apellidos y edades de las personas, que han cargado sus datos. 
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)
    contador += 1 #Nos va a permitir aumentar el valor, en este caso seria la cantidad de personas, que van ingresando al programa. Es decir, se va contando la cantidad de personas. Pero llegara hasta 5 y no permitira mas intentos.
print("El programa esta diseñado para solamente ingresen cinco personas.")
