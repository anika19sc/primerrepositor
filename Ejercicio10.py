"""Escribe un programa que calcule el promedio general de una clase."""
cont = 0 #Es un operador tipo contador.
sumatoria_de_las_notas = 0 #Es un operador tipo acumulador, lo que va hacer es sumar todas las notas.
cant_alumnos_clase = int(input("¿Cuantos alumnos tiene en su clase y quiere conocer el promedio?")) #El usuario ingresa la cantidad de alumnos que desea, para sacar el promedio.
#Usaremos una estructura iterativa, while, lo que va hacer es permitir repetir el programa, para la cantidad de personas que de ante mano el usuario hizo saber.
while cont <= cant_alumnos_clase:
    calificacioon = int(input("Ingrese la nota del estudiante: ")) #El usuario ingresa las notas una por una.
    cont +=1 #Aca lo que va hacer el contador es una vez que hace el paso anterior (ingresar nota del estudiante), va sumando. Osea hace el paso anterior y luego cuenta 1, hace el paso anterior y luego a ese 1 le suma una mas, y asi repetitivamente. Hasta que llegue al tope de la cantidad de los alumnos que el usuario quiere conocer. 
    sumatoria_de_las_notas = sumatoria_de_las_notas + calificacioon #Lo que vamos hacer en esta variable, es acumular la suma de las calificaciones.
    promedio_general = sumatoria_de_las_notas/cant_alumnos_clase #Lo que vamos hacer acontinuacion en esta variable, es calcular el promedio general, que seria sumar las notas y dividir por la cantidad de alumnos.
print("El promedio general de la clase es: ", promedio_general) #Para finalizar mostramos el promedio general.