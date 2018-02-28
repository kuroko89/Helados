class MaquinaHelado:
    def __init__(self):
        self._disponibilidad=True
        self._sabor="Vainilla"
    def servir(self):
        print("un helado de"+self._sabor)
    def setDisponibilidad(self,disponibilidad):
        self._disponibilidad=disponibilidad
    def getDisponibilidad(self):
        return self._disponibilidad
    def setSabor(self,sabor):
        self._sabor=sabor
    def getSabor(self):
        return self._sabor
