from classEmpleado import Empleados
from classArea import Area

class Directores(Empleados, Area):
    def __init__(self):
        super().__init__()
        self._region = ""
        self._presupuestoAnual = 0
        self._capitalInvertido = 0

    # Getter y Setter
    def getRegion(self):
        return self._region

    def setRegion(self, region):
        self._region = region

    def getPresupuesto(self):
        return self._presupuestoAnual

    def setPresupuesto(self, presupuestoAnual):
        self._presupuestoAnual = presupuestoAnual

    def getCapitalInv(self):
        return self._capitalInvertido

    def setCapitalInv(self, capitalInvertido):
        self._capitalInvertido = capitalInvertido

    def mostrarInfoDirector(self):
        parentInfo = super().mostrarInfoEmpleado()
        parent2Info = super().mostrarInfoArea()
        return f"{parentInfo} {parent2Info} La region del director es: {self._region}, Presupuesto anual: {self._presupuestoAnual}, Capital invertido: {self._capitalInvertido}"