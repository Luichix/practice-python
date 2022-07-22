import pickle

class Vehiculo():
    
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arranque = False
        self.acelera = False
        self.frena = False

    def arrancar(self, arrancamos):
        self.arranque= arrancamos

    def acelerar(self, aceleramos):
        self.acelera = aceleramos
    
    def frenar(self, frenamos):
        self.frena= frenamos

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nArranque: ", self.arranque,
        "\nAcelera: ", self.acelera, "\nFrena: ", self.frena )

Coche1 = Vehiculo("Toyota","Hilux")

Coche1.acelerar(True)

Coche1.estado()

