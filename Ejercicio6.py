"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto+bonif)
a. Si trabajo más de 120hs por mes, la bonificación es de %18
b. Si trabajo entre 80 y 120hs, la bonificación es de %15
c. Si trabajo menos de 80hs, la bonificación es de %13"""

cant_horas_trabajadas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #El usuario debe ingresar cuantas horas trabajo en el mes.
if cant_horas_trabajadas > 120 and cant_horas_trabajadas < 150:#Si el usuario trabaja más de 120 horas con un limite 150 horas, pasamos a la siguiente operacion.
    mul_sueldo_mes = cant_horas_trabajadas * 1500  #Multiplicamos las horas por 1500.
    oper_bonificacion= mul_sueldo_mes *0.18 #Luego multiplicamos el sueldo mensual por la bonificacion que corresponde del %18.
elif cant_horas_trabajadas > 80 and cant_horas_trabajadas <= 120: 
    mul_sueldo_mes = cant_horas_trabajadas * 1300 #Si el usuario trabaja entre 80 hasta 120. Multiplico las horas por 1300.
    oper_bonificacion=mul_sueldo_mes * 0.15 #Luego multiplicamos el sueldo mensual por la bonificacion que corresponde del %15.
elif cant_horas_trabajadas <= 80: 
    mul_sueldo_mes = cant_horas_trabajadas * 1100 #Si el usuario trabaja menos de 80 horas. Multiplico las horas por 1100.
    oper_bonificacion=mul_sueldo_mes*0.13 #Multiplicamos el sueldo mensual por la bonificacion que corresponde del %13.
else: 
    print("Error") #Si el usuario se equivoca con los numeros y pone por error cualquier cosa, le va saltar que es error.

sueldo_neto =mul_sueldo_mes + oper_bonificacion #Aca vamos hacer la operacion para sacar el sueldo neto: que seria sumando el sueldo bruto que es la cantidad de horas trabajadas en el mes, mas la bonificacion.

print("*Su sueldo bruto es de:", mul_sueldo_mes, "\n","*Por las horas que trabajo, usted tiene una bonificacion que es de:", oper_bonificacion, "\n","*Por la cantidad de horas que trabajo mas la bonificacion. Sueldo neto es de:", sueldo_neto) #Por ultimo, le damos el resultado final del programa al usuario. 