# main.py
from classDirector import Directores
from classGerente import Gerentes
from classJefeArea import JefeArea

def main():
    # Crear objetos
    director = Directores()
    director.set_nombre("Johana")
    director.set_apellido("Martinez")
    director.set_edad(25)
    director.setCargo("Director")
    director.setSueldo(50000)
    director.setNomina("ROHA56")
    director.setNombreA("Almacen")
    director.setUbicacion("Piso 2")
    director.setTurno("Matutino")
    director.setRegion("Pachuca")
    director.setPresupuesto(23000000)
    director.setCapitalInv(45678976)
    director.setNombreDepa("Z")
    director.setId(234)
    director.setDireccion("Calle 127")

    gerente = Gerentes()
    gerente.set_nombre("Pedro")
    gerente.set_apellido("Sanchez")
    gerente.set_edad(19)
    gerente.setCargo("Gerente")
    gerente.setSueldo(3000)
    gerente.setNomina("PDE45")
    gerente.setNombreA("Finanzas")
    gerente.setUbicacion("Piso 4")
    gerente.setTurno("Vespertino")
    gerente.setNombreDepa("Y")
    gerente.setId(67)
    gerente.setDireccion("Col 127")
    gerente.setSucursales(45)
    gerente.setVentasMen(340)
    gerente.setInventarioT(45678)

    jefeArea = JefeArea()
    jefeArea.set_nombre("Ashley")
    jefeArea.set_apellido("Contreras")
    jefeArea.set_edad(20)
    jefeArea.setCargo("Jefe")
    jefeArea.setSueldo(5000)
    jefeArea.setNomina("AH34")
    jefeArea.setNombreA("Recursos")
    jefeArea.setUbicacion("Piso 2")
    jefeArea.setTurno("Matutino")
    jefeArea.setNombreDepa("R")
    jefeArea.setId(579)
    jefeArea.setDireccion("Calle 12")
    jefeArea.setNivelEfi(80)
    jefeArea.setTiempoRe(30)
    jefeArea.setNivelRotInv(50)


    print("Director")
    print(director.mostrarInfoDirector())
    print("\nGerente")
    print(gerente.mostrarInfoGerente())
    print("\nJefe de Area")
    print(jefeArea.mostrarInfoJefe())

if __name__ == "__main__":
    main()