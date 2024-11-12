from classPersona import Persona

class Empleados(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._sueldo = 0
        self._nomina = ""

    # Getter y Setter
    def getCargo(self):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSueldo(self):
        return self._sueldo

    def setSueldo(self, sueldo):
        self._sueldo = sueldo

    def getNomina(self):
        return self._nomina

    def setNomina(self, nomina):
        self._nomina = nomina

    def mostrarInfoEmpleado(self):
        parentInfo = super().mostrarInfoPersona()
        return f"{parentInfo}, Cargo: {self._cargo}, Sueldo: {self._sueldo}, Nómina: {self._nomina}"