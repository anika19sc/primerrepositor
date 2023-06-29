"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80hs por mes, la hora tiene un valor de $1100"""

cant_horas_trabajadas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #El usuario debe ingresar cuantas horas trabajo en el mes.
if cant_horas_trabajadas > 120 and cant_horas_trabajadas < 150:#Si el usuario trabaja más de 120 horas con un limite 150 horas, pasamos a la siguiente operacion.
    mul_sueldo_mes = cant_horas_trabajadas * 1500  #Multiplicamos las horas por 1500.

elif cant_horas_trabajadas > 80 and cant_horas_trabajadas <= 120: 
    mul_sueldo_mes = cant_horas_trabajadas * 1300 #Si el usuario trabaja entre 80 hasta 120. Multiplico las horas por 1300.
elif cant_horas_trabajadas <= 80: 
    mul_sueldo_mes = cant_horas_trabajadas * 1100 #Si el usuario trabaja menos de 80 horas. Multiplico las horas por 1100.
    
print ("Tu sueldo es de:", mul_sueldo_mes ,"pesos, por las horas que trabajaste.")#Damos a conocer el resultado al usuario de cuanto cobra por mes. 