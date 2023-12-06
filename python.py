"""Module providing a function printing python version."""
usuario = input("Ingrese usuario")
clave = input("Ingrese el codigo")
botellas_miel = float(input("Cuantas botellas de miel desea?"))
precio = float(input("De que precio desea?"))
total = botellas_miel * precio
print("Para", usuario, "el codigo es", clave, usuario, "lleva ",
      botellas_miel, " botellas de miel", "El precio a pagar es",
      total)

pago = int(input(
    "seleccione metodo de pago: Para tarjeta presione 1, para efectivo presione 2, para transferencia presione 3"))
if pago == 1:
    tarjeta = int(input("introduzca su tarjeta"))
    print(tarjeta)
elif pago == 2:
    print("Por favor cancelar en su distribuidor mas cercano")
elif pago == 3:
    referencia_bancaria = int(
        input("Introduzca el numero de su referencia bancaria "))
    print("La referencia es", referencia_bancaria)
else:
    print("La opción que marcó no es correcta")
