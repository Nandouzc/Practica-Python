"""cajero"""
class cajero:
    monto = 50000
    print("Bienvenido a su cajero")
    def operaciones(self):
        self.opcion = int(input("""======================
        Por favor indique que operacion desea realizar : 
        1-Consultar saldo
        2-Depositar
        3-Retirar efectivo
        4-Salir                        """))
        self.control = 0
        while self.control==0:
            if self.opcion==1:
                self.consultar_balance()
            if self.opcion==2:
                self.depositar()
            if self.opcion==3:
                self.retirar()
            if self.opcion==4:
                self.control = 1
                self.salir()
            else:
                print("Lo sentimos la opcion que eligio no es valida")
                self.operaciones()
    
    def consultar_balance(self):
        print(f"Su balance es:{self.monto}")
        print("Desea realizar otra operacion?")
        self.operaciones()
    
    def depositar(self):
        self.deposito = int(input("Ingrese el monto que desea depositar"))
        self.monto = self.monto + self.deposito
        self.consultar_balance()

    def retirar(self):
        self.retiro = int(input("Ingrese el monto que desea retirar"))
        if self.retiro>self.monto:
            print("Lo sentimos no cuenta con fondos suficientes")
            self.retirar()
        else:
            self.monto = self.monto - self.retiro
            print(f"Su retiro fue de {self.retiro}")
            self.consultar_balance()

    def salir(self):
        print("=================================================================")
        print("Gracias por usar nuestros servicios")
        print("=================================================================")
            
ejecucion = cajero()            
ejecucion.operaciones()