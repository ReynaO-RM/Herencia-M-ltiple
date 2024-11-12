from classEmpleado import Empleados
from classArea import Area

class Gerentes(Empleados, Area):
    def __init__(self):
        super().__init__()
        self._sucursales = 0
        self._ventasMensuales = 0
        self._inventarioTotal = 0

    # Getter y Setter
    def getSucursales(self):
        return self._sucursales

    def setSucursales(self, sucursales):
        self._sucursales = sucursales

    def getVentasMen(self):
        return self._ventasMensuales

    def setVentasMen(self, ventasMensuales):
        self._ventasMensuales = ventasMensuales

    def getInventarioT(self):
        return self._inventarioTotal

    def setInventarioT(self, inventarioTotal):
        self._inventarioTotal = inventarioTotal

    def mostrarInfoGerente(self):
        parentInfo = super().mostrarInfoEmpleado()
        parent2Info = super().mostrarInfoArea()
        return f"{parentInfo} {parent2Info} Número de sucursales: {self._sucursales}, Ventas mensuales: {self._ventasMensuales}, Inventario total: {self._inventarioTotal}"
