"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)."""
nota1 = int(input("Ingrese la primer nota: ")) #Le pedimos al usuario que coloque la nota que saco en su primer parcial.
nota2 = int(input("Ingrese la segunda nota: ")) #El usuario coloca la nota que saco en su segundo parcial.
nota3 = int(input("Ingrese la tercer nota: ")) #El usuario ingresa la nota de su ultimo parcial.
prom = (nota1 + nota2 + nota3) / 3 #Aca se realiza la operacion para calcular el promedio. Sumamos las notas y las dividimos por tres.

if prom > 6: #Si el resultado de la operacion anterior, es mayor que seis, el alumno regulariza la materia.
    print ("El alumno aprobó la materia. El resultado de su promedio es:", prom)
#Si el alumno en su promedio saco menor que seis, en la operacion anterior, no aprobo la materia.
else:
    print ("El alumno recursa la materia. El resultado de su promedio es:", prom)