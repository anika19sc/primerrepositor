"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""
cant_dolares= int(input("Ingrese cantidad de dólares a convertir: ")) #Aca le pediremos al usuario que ingrese cuantos dólares desea convertir.
valor_dolar_actual = int(input("Ingrese valor del dólar actual: ")) #El usuario debe ingresar el valor actual del dólar.
money_argentina = cant_dolares * valor_dolar_actual #En este fragmento haremos la operacion de multiplicar la cantidad de dolares por el valor actual del dolar. Esto nos dara el monto que el usuario quiere estimar en pesos.
print("El equivalente en pesos seria: ", money_argentina) #Le mostramos por pantalla al usuario el resultado de la operacion, de la conversion dolar en pesos.