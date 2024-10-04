class CuentaCorriente:
    def __init__(self,nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo
    
    def depositar(self, monto):
        if monto>0:
            self.saldo += monto
            print (f"Depositado ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("monto a depositar invalido.")
            
    def retirar(self,monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"retira $ {monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("saldo insuficiente o monto invalido.")
            
    def get_saldo(self):
        return self.saldo
    
    
cuenta= CuentaCorriente("Juana", 1000)

print(f"Dueño de cuenta: {cuenta.nombre}")
print(f"Saldo inicial: ${cuenta.get_saldo()}")

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(1500)

print(f"Saldo final: ${cuenta.get_saldo}")