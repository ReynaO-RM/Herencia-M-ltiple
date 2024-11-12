from classEmpleado import Empleados
from classArea import Area

class JefeArea(Empleados, Area):
    def __init__(self):
        super().__init__()
        self._nivelRotacionInven = 0
        self._nivelEficiencia = 0
        self._tiempoReabastecimiento = 0

    # Getter y Setter
    def getNivelRotInv(self):
        return self._nivelRotacionInven

    def setNivelRotInv(self, nivelRotacionInven):
        self._nivelRotacionInven = nivelRotacionInven

    def getNivelEfi(self):
        return self._nivelEficiencia

    def setNivelEfi(self, nivelEficiencia):
        self._nivelEficiencia = nivelEficiencia

    def getTiempoRe(self):
        return self._tiempoReabastecimiento

    def setTiempoRe(self, tiempoReabastecimiento):
        self._tiempoReabastecimiento = tiempoReabastecimiento

    def mostrarInfoJefe(self):
        parentInfo = super().mostrarInfoEmpleado()
        parent2Info = super().mostrarInfoArea()
        return f"{parentInfo} {parent2Info} Nivel de Rotacion de inventario: {self._nivelRotacionInven}, Nivel de eficiencia: {self._nivelEficiencia}%, Tiempo de reabastecimiento: {self._tiempoReabastecimiento} dias"
