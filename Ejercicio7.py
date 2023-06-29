"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de
horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año."""

print("Bienvenido querido empleado, acontinuacion mostraremos su recibo de sueldo. Segun las horas que trabajo en el mes, le mostraremos una aproximacion de lo que ganara por doce meses de trabajo.")

cant_horas_trabajadas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #El usuario debe ingresar cuantas horas trabajo en el mes.
if cant_horas_trabajadas > 120 and cant_horas_trabajadas <=130 :#Si el usuario trabaja más de 120 horas con un limite 130 horas, pasamos a la siguiente operacion.
    mul_sueldo_mes = cant_horas_trabajadas * 1500  #Multiplicamos las horas por 1500.
    oper_bonificacion= mul_sueldo_mes *0.18 #Luego multiplicamos el sueldo mensual por la bonificacion que corresponde del %18.
    print("Querido Empleado: Le informamos que aplicamos una bonificacion del %18. Ademas, le hacemos saber que la hora tiene un valor de $1.500")

elif cant_horas_trabajadas > 80 and cant_horas_trabajadas <= 120: 
    mul_sueldo_mes = cant_horas_trabajadas * 1300 #Si el usuario trabaja entre 80 hasta 120. Multiplico las horas por 1300.
    oper_bonificacion=mul_sueldo_mes * 0.15 #Luego multiplicamos el sueldo mensual por la bonificacion que corresponde del %15.
    print("Querido Empleado: Le informamos que aplicamos una bonificacion del %15. Ademas, le hacemos saber que la hora tiene un valor de $1.300")

elif cant_horas_trabajadas <= 80: 
    mul_sueldo_mes = cant_horas_trabajadas * 1100 #Si el usuario trabaja menos de 80 horas. Multiplico las horas por 1100.
    oper_bonificacion=mul_sueldo_mes*0.13 #Multiplicamos el sueldo mensual por la bonificacion que corresponde del %13.
    print("Querido Empleado: Le informamos que aplicamos una bonificacion del %13. Ademas, le hacemos saber que la hora tiene un valor de $1.100")

else: 
    print("Error. Ingrese de nuevo.") #Si el usuario se equivoca con los numeros y pone por error cualquier cosa, le va saltar que es error.

sueldo_neto =mul_sueldo_mes + oper_bonificacion #Aca vamos hacer la operacion para sacar el sueldo neto: que seria sumando el sueldo bruto que es la cantidad de horas trabajadas en el mes, mas la bonificacion.
print("Recibo de sueldo mensual. Cuenta con:")
print("*Sueldo bruto de:", mul_sueldo_mes, "\n","*Bonificacion de:", oper_bonificacion, "\n","*Sueldo neto de:", sueldo_neto, "\n" "") #Por ultimo, le damos el resultado final del programa al usuario. 

sueldo_anual= mul_sueldo_mes * 12 #En este fragmento multiplicamos las horas trabajadas mensuales (que se convierte en el sueldo bruto) por 12, que da como resultado el sueldo anual bruto que el usuario debe cobrar.
horas_trabajo_anual= cant_horas_trabajadas * 12 #Aca hacemos la operacion antes, de multiplicar las horas que trabajo el usuario por 12. De esta manera sacamos la cantidad de horas que trabajo el usuario en el año.
bonificacion_anual= oper_bonificacion * 12 #Aca haremos la operacion para calcular el monto anual de bonificacion.

if sueldo_anual > 2000000 and sueldo_anual <=2500000: #Si el total del sueldo anual es mayor que dos millones con un limite de dos millones quinientos mil...
    descuento= sueldo_anual * 0.05 #Entonces se le hara un descuento del %5. 
    print("Informamos que usted entro en el plazo de trabajo al cual denominamos clase alta. Se le aplica un descuento del %5")

elif sueldo_anual >=1000000 and sueldo_anual <=2000000: #Sino el total del sueldo anual es mayor que un millon y menor que dos millones...
    descuento=sueldo_anual * 0.03 #Entonces se le hara un descuento del %3.
    print("Informamos que usted entro en el plazo de trabajo al cual denominamos clase media. Se le aplica un descuento del %3")

elif sueldo_anual < 1000000: #Sino el total del sueldo anual es menor a un millon...
    descuento=sueldo_anual * 0.01 #Entonces se le hara un descuento del %1.
    print("Informamos que usted entro en el plazo de trabajo al cual denominamos clase baja. Se le aplica un descuento del %1")

print("Recibo de sueldo anual. Cuenta con:")
print("*Salario bruto de:", sueldo_anual, "\n","*Monto de bonificacion de:",bonificacion_anual, "\n","*Descuento de:", descuento, "\n" "*Aproximacion de la cantidad de horas que deberia trabajar:", horas_trabajo_anual) #Por ultimo, el programa le dara el resultado al usuario. 
