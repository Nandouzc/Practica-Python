"""Probando python"""
# pintor = "Francisco"
# status = " Esta ocupado"
# pintor_availability = f"{pintor} {status}"
# print(pintor_availability.center(50))
# print(pintor_availability.replace("ocupado","muy ocupado"))


# n1 = int(input("ingresar primer numero"))
# n2 = int(input("ingresar segundo numero"))
# suma = n1 + n2
# resta = n1 - n2
# multi = n1 * n2
# div = n1 / n2
# mensaje = f""" Para los números {n1} y {n2}, 
# El resultado de la suma es {suma}.
# El resultado de la resta es {resta}.
# El resultado de la multiplicación es {multi}.
# El resultado de la división es {div}.
# """
# print(mensaje)



# colors = ["green","blue","red"]
# colors.append("violet")
# colors.extend(["orange", "teal"])
# colors.insert(2 , "pink")
#  print(colors)



# count = 1
# while count<=10:
#     print(count)
#     count += 1



# produccion = 0
# for f in range(5):
#     valor = int(input("ingrese la produccion por colmena"))
#     produccion = produccion + valor
# print("La produccion total es: ", produccion)
# promedio = produccion/5
# print("El promedio por colmena es: ", promedio)



# arroba = "@"
# cantidad = 0
# mail = input("Ingrese su correo...")
# for f in mail:
#     if f==arroba:
#         cantidad += 1
# if cantidad>=1: 
#     print("Su correo es", mail)   
# else :
#     print("El correo que ingresó no es correcto")


# valor = int(input("Ingrese el numero de la tabla"))
# if valor<=10 :
#     print("Selecciono la tabla del",valor)
#     for multi in range(11) :
#         print(valor, "X", multi, "=", multi*valor  )
# else :
#     print("La tabla que selecciono no es correcta")    


# def suma():
#     n1 = int(input("Ingrese un numero "))
#     n2 = int(input("Ingrese otro numero "))
#     print(f"El resultado es {n1 + n2}")

# suma()



# def crear_contraseña(num):
#     chars = "ghvfgdhhuj"
#     numero_entero = str(num)
#     num = int(numero_entero[0])
#     c1 = num - 2
#     c2 = num
#     c3 = num + 5 
#     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}" 
#     return contraseña

# password = crear_contraseña(3)
# frase = f"Tu contraseña es {password}"
# print(frase)







# def generaPares(limite):
#     num = 1
#     while num<limite:
#         yield num*2
#         num+=1

# devuelve_pares = generaPares(5)
# print(next(devuelve_pares))        
# print("texto")
# print(next(devuelve_pares))



list = []

while True:   
    numero= input("ingrese un numero, escriba listo cuando esten todos los numeros ")
    if numero.lower()=="listo":
        break
    numero = int(numero)
    
    list.append(numero)
mayor = None

for numero in list:
    if mayor==None:
        mayor = numero
    else :
        if numero>mayor:
            mayor = numero
print(f"El numero mayor es : {mayor}")           