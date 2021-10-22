# punto 1
print("Punto 1")
print("Defina la edad")
edad = int(input())
if edad > 17:
    print("Debe sacar la cédula")
else:
    print("Aun no debe sacar la cédula")

# punto 2
print('\n', "Punto 2")
print("Ingrese un número")
num = int(input())
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")

# punto 3
print('\n', "Punto 3")
print("Ingrese un número")
num = int(input())
if num > 100:
    print("El número es mayor de 100")
else:
    print("El número es menor de 100")

# punto 4
print('\n', "Punto 4")
print("Ingrese un número de horas trabajadas")
horas = int(input())
if horas <=40 :
    print("El salario semanal es {}".format(horas*300))
else:
    horas_extra = horas-40
    print("El salario semanal es {}".format(horas*300+horas_extra*500))

# punto 5
print('\n', "Punto 5")
print("Ingrese un número del 1 al 7")
dia = int(input())
if dia==1:
    print('Lunes')
elif dia==2:
    print('Martes')
elif dia==3:
    print('Miércoles')
elif dia==4:
    print('Jueves')
elif dia==5:
    print('Viernes')
elif dia==6:
    print('Sábado')
else:
    print('Domingo')

# punto 6
print('\n', "Punto 6")
print("Ingrese el usuario")
usuario = input()
if len(usuario)==0:
    print("Ingrese un usuario válido")
print("Ingrese la contraseña")
contraseña = input()
if len(contraseña)==0:
    print("Ingrese una contraseña válida")
if len(usuario)>0 and len(contraseña)>0:
    print("login exitoso!")
else:
    print("login sin exito")

# punto 7
print('\n', "Punto 7")
print("Ingrese el último número de la placa")
num = int(input())
if num==0 or num==1:
    print("Tiene pico y placa el lunes")
elif num==2 or num==7:
    print("Tiene pico y placa el martes")
elif num==9 or num==4:
    print("Tiene pico y placa el miercoles")
elif num==5 or num==3:
    print("Tiene pico y placa el jueves")
else:
    print("Tiene pico y placa el viernes")

# punto 8
print('\n', "Punto 8")
print("Ingrese una letra")
letra = input().lower()
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("la letra es una vocal")
else:
    print("la letra no es una vocal")

# punto 9
print('\n', "Punto 9")
print("Ingrese una opción")
opcion = input().lower()
if opcion=="archivo" or opcion=="buscar" or opcion=="salir":
    print("OK")
else:
    print("No introdujo una opción correcta")