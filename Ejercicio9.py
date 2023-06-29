"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresadas por el usuario."""
personas = int(input("¿Cuantas personas desea ingresar?: "))#Se le pregunta al usuario la cantidad de personas que desea saber sus datos.
contador = 1
while contador <= personas: #Quiere decir la cantidad de personas ingresadas por el usuario.
    print("Persona", contador) #Va contando las personas que ingresan.
    nombre = str(input("Ingrese un nombre: ")) #Ingreso de datos.
    apellido = str(input("Ingrese un apellido: ")) #Ingreso de datos.
    edad = int(input("Ingrese una edad: ")) #Finaliza el ingreso de datos.
    #Lo siguiente, muestra al usuario los datos cargados. 
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)
    contador += 1
print("El programa finalizo, solo cargaron sus datos:",personas)