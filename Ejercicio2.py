"""Escribe un programa que calcule el área y el perimetro de un cuadrado y muestre los resultados (Indicando cuál es cuál) por pantalla."""
lado = int(input("Ingrese el lado de un cuadrado: ")) #Aca le pidemos al usuario que ingrese el lado de un cuadrado.
area = lado * lado #Haremos la operacion que seria multiplicar lado por lado para obtener el area.
perim = lado * 4 #Aca multiplicamos la variable lado por cuatro para que nos de como resultado el perimetro.
print ("El area del cuadrado es: ", area) 
print ("El perimetro del cuadrado es: ", perim)
#Por ultimo le damos a conocer al usuario el programa que pidio.