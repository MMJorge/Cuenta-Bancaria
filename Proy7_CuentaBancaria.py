class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}\nNº Cuenta: {self.numero_cuenta}\nBalance: {self.balance}€'

    def depositar(self,cantidad_ingreso):
        self.balance += cantidad_ingreso
        print('Depósito aceptado')

    def retirar(self,cantidad_retiro):
        if self.balance >= cantidad_retiro:
            self.balance -= cantidad_retiro
            print('Operación realizada correctamente')
        else:
            print('Dinero insuficiente')

def crear_cliente():
    nombre_cl = input('Por favor, dime tu nombre: ')
    apellido_cl = input('Por favor, dime tu apellido: ')
    numero_cuenta_cl = input('Ahora, por favor, dime tu numero de cuenta: ')
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta_cl)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            cantidad_depositar = int(input('Cantidad a depositar: '))
            mi_cliente.depositar(cantidad_depositar)
        elif opcion == 'R':
            cantidad_retirar = int(input('cantidad a retirar: '))
            mi_cliente.retirar(cantidad_retirar)
        print(mi_cliente)

    print('Gracias por operar en Banco Python')

inicio()



