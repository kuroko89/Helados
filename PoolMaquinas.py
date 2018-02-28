from MaquinaHelado import*
class PoolMaquinas(object):
    _instancia=None
    def __new__(self):
        if self._instancia==None:
            self._instancia= super(PoolMaquinas, self).__new__(self)
            self._Maquinas=[]
            for i in range (1,11):
                self._Maquinas.append(MaquinaHelado())
        return self._instancia
    def pedirMaquinas(self):
        temp = False
        for maquina in self._Maquinas:
            if maquina.getDisponibilidad():
                temp=True
                maquina.setDisponibilidad(False)
                return maquina
                break
        if temp==False:
            print("no hay maquinas disponibles")
    def devolverMaquina(self):
        for maquina in self._Maquinas:
            if maquina.getDisponibilidad()==False:
                maquina.setDisponibilidad(True)
                break
    def pedirInstancia(self):
        self.__new__()
    def getMaquinas(self):
        temp = 0
        for maquina in self._Maquinas:
            if maquina.getDisponibilidad()==True:
                temp=temp+1
        return temp







