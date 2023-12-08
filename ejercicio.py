"""clacu"""
n1 = ""
print("Bienvenido a la calculadora, para salir escribe salir")
print("Las operciones son: suma, resta, multi y div")
while True:
    if not n1 :
        n1 = input("ingrese un numero: ")
        if n1.lower()=="salir":
            break
        n1 = int(n1)
    else:
        operacion = input("Ingrese una operacion: ")
        if operacion.lower()=="salir":
            break
        n2 = (input("Ingrese el segundo numero: "))
        if n2.lower()=="salir":
            break
        n2 = int(n2)
        if operacion == "suma" :
            n1 += n2
        elif operacion == "resta" :
            n1 -= n2
        elif operacion == "multi" :
            n1 *= n2
        elif operacion == "div" :
            n1 /= n2
        else: 
            print("Operacion no valida")
            break
        print(f"El resultado es: {n1}")    