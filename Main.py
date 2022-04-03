import pickle
import os
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   UNDERLINE = '\033[4m'

archivoTexto = "CUMPLES.dat"

with open(archivoTexto,"wb") as archivo:
    lista = []
    pickle.dump(lista, archivo)

nombre = str(input("Introduzca un nombre de pila: "))
dia = int(input("Introduzca el día de su cumpleaños: "))
mes = int(input("Introduzca el mes de su cumpleaños: "))
with open(archivoTexto,"rb") as archivo:
    datos = pickle.load(archivo)
with open(archivoTexto,"wb") as archivo:
    pickle.dump(datos,archivo)
    print ()
    print (color.BOLD + "Registro grabado en el fichero" + color.END)
    print()

nombre1 = str(input("Introduzca un nombre de pila: "))
dia1 = int(input("Introduzca el día de su cumpleaños: "))
mes1 = int(input("Introduzca el mes de su cumpleaños: "))
with open(archivoTexto,"rb") as archivo:
    datos = pickle.load(archivo)
with open(archivoTexto,"ab") as archivo:
    pickle.dump(datos,archivo)
    print ()
    print (color.BOLD + "Registro grabado en el fichero" + color.END)
    print()

nombre2 = str(input("Introduzca un nombre de pila: "))
dia2 = int(input("Introduzca el día de su cumpleaños: "))
mes2 = int(input("Introduzca el mes de su cumpleaños: "))
with open(archivoTexto,"rb") as archivo:
    datos = pickle.load(archivo)
with open(archivoTexto,"ab") as archivo:
    pickle.dump(datos,archivo)
    print ()
    print (color.BOLD + "Registro grabado en el fichero" + color.END)
    print()

nombre3 = str(input("Introduzca un nombre de pila: "))
dia3 = int(input("Introduzca el día de su cumpleaños: "))
mes3 = int(input("Introduzca el mes de su cumpleaños: "))
with open(archivoTexto,"rb") as archivo:
    datos = pickle.load(archivo)
with open(archivoTexto,"ab") as archivo:
    pickle.dump(datos,archivo)
    print ()
    print (color.BOLD + "Registro grabado en el fichero" + color.END)
    print()

nombre4 = str(input("Introduzca un nombre de pila: "))
dia4 = int(input("Introduzca el día de su cumpleaños: "))
mes4 = int(input("Introduzca el mes de su cumpleaños: "))
with open(archivoTexto,"rb") as archivo:
    datos = pickle.load(archivo)
with open(archivoTexto,"ab") as archivo:
    pickle.dump(datos,archivo)
    print ()
    print (color.BOLD + "Registro grabado en el fichero" + color.END)
    print()


print("Introduzca la fecha de hoy")
day = int(input("Día: "))
month = int(input("Mes: "))
year = int(input("Año: "))
print()
print("La fecha de cumpleaños de " + str(nombre) + " es el " + str(dia) + "/" + str(mes))
if day != dia:
    if month != mes:
        print(color.BOLD + "Un poquito despistado, ¿no? Ni día ni mes" + color.END)
    if month == mes:
        print(color.BOLD + "Me temo que el mes coincide pero el día no" + color.END)
if day == dia:
    if month != mes:
        print(color.BOLD + "Me temo que el día coincide pero el mes no" + color.END)
    if month == mes:
        print(color.BOLD + "¡¡¡FELIZ, FELIZ EN TU DÍA...!!!" + color.END)

print()
print("La fecha de cumpleaños de " + str(nombre1) + " es el " + str(dia1) + "/" + str(mes1))
if day != dia1:
    if month != mes1:
        print(color.BOLD + "Un poquito despistado, ¿no? Ni día ni mes" + color.END)
    if month == mes1:
        print(color.BOLD + "Me temo que el mes coincide pero el día no" + color.END)
elif day == dia1:
    if month != mes1:
        print(color.BOLD + "Me temo que el día coincide pero el mes no" + color.END)
    if month == mes1:
        print(color.BOLD + "¡¡¡FELIZ, FELIZ EN TU DÍA...!!!" + color.END)

print()
print("La fecha de cumpleaños de " + str(nombre2) + " es el " + str(dia2) + "/" + str(mes2))
if day != dia2:
    if month != mes2:
        print(color.BOLD + "Un poquito despistado, ¿no? Ni día ni mes" + color.END)
    if month == mes2:
        print(color.BOLD + "Me temo que el mes coincide pero el día no" + color.END)
elif day == dia2:
    if month != mes2:
        print(color.BOLD + "Me temo que el día coincide pero el mes no" + color.END)
    if month == mes2:
        print(color.BOLD + "¡¡¡FELIZ, FELIZ EN TU DÍA...!!!" + color.END)

print()
print("La fecha de cumpleaños de " + str(nombre3) + " es el " + str(dia3) + "/" + str(mes3))
if day != dia3:
    if month != mes3:
        print(color.BOLD + "Un poquito despistado, ¿no? Ni día ni mes" + color.END)
    if month == mes3:
        print(color.BOLD + "Me temo que el mes coincide pero el día no" + color.END)
elif day == dia3:
    if month != mes3:
        print(color.BOLD + "Me temo que el día coincide pero el mes no" + color.END)
    if month == mes3:
        print(color.BOLD + "¡¡¡FELIZ, FELIZ EN TU DÍA...!!!" + color.END)

print()
print("La fecha de cumpleaños de " + str(nombre4) + " es el " + str(dia4) + "/" + str(mes4))
if day != dia4:
    if month != mes4:
        print(color.BOLD + "Un poquito despistado, ¿no? Ni día ni mes" + color.END)
    if month == mes4:
        print(color.BOLD + "Me temo que el mes coincide pero el día no" + color.END)
elif day == dia4:
    if month != mes4:
        print(color.BOLD + "Me temo que el día coincide pero el mes no" + color.END)
    if month == mes4:
        print(color.BOLD + "¡¡¡FELIZ, FELIZ EN TU DÍA...!!!" + color.END)