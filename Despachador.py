from PoolMaquinas import *
class Despachador:
    def __init__(self):
        self._poolMaquinas=PoolMaquinas()
        self.boleano=True
        self._maquinasUsuario=[]
    def interactuar(self):
        while True:
            entrada=input("digite a para pedir maquina, b para devolverla")
            if entrada=="a":
                self._maquinasUsuario.append(self._poolMaquinas.pedirMaquinas())
            else:
                self._poolMaquinas.devolverMaquina()
            print(self._poolMaquinas.getMaquinas())

