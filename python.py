"""Python"""
usuario = input("Ingrese usuario: ")
codigo = input("Ingrese el codigo: ")
botellas_miel = float(input("Cuantas botellas de miel desea?: "))
precio = float(input("De que precio desea?: "))
total = botellas_miel * precio
print("Para", usuario, "el codigo es", codigo,",", usuario, "lleva ",
      botellas_miel, " botellas de miel",",", "El precio a pagar es",
      total)

finish= False
while finish is False:
    pago = int(input(
    """seleccione metodo de pago: Para tarjeta presione 1,
      para efectivo presione 2, para transferencia presione 3 """))
    if pago == 1:
        tarjeta = int(input("introduzca su tarjeta "))
        print("Operacion exitosa")
        finish= True
    elif pago == 2:
        print("Por favor cancelar en su distribuidor mas cercano")
        print("Esperamos su visita")
        finish= True
    elif pago == 3:
        referencia_bancaria = int(
        input("Introduzca el numero de su referencia bancaria "))
        print("La referencia es", referencia_bancaria)
        finish= True
    else:
        print("La opción que marcó no es correcta ")
