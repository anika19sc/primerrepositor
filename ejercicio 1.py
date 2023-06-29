"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento."""
anuario= int(input("Ingrese el año que en nació:")) #Se le pide al usuario que coloque el año de su nacimiento.
anuario_presente= int(input("Ingrese el año presente")) #Se le pide al usuario que ingrese el año actual.
age= anuario_presente-anuario #Aca haremos la operación que seria restar el año que nacio, menos el año actual, para que saber la edad que cumple este año.
print("Usted tiene o va a cumplir:", age)#Al final le va aparecer al usuario la edad que cumplira este año.