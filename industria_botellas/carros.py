    #************ Ejercicio POO - Carros ***************

class Carros:
    def __init__(self):
        self.__modelo = ""
        self.__color = ""
        self.__motor = ""
        self.__numero_puertas = 0
        self.__capacidad_pasajeros = 0
        self.__tipo_combustible = ""

    #************* Encapsulamiento: Getters y Setters **************
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_motor(self):
        return self.__motor

    def set_motor(self, motor):
        self.__motor = motor

    def get_numero_puertas(self):
        return self.__numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self.__numero_puertas = numero_puertas

    def get_capacidad_pasajeros(self):
        return self.__capacidad_pasajeros

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.__capacidad_pasajeros = capacidad_pasajeros

    def get_tipo_combustible(self):
        return self.__tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self.__tipo_combustible = tipo_combustible

    def asignar_datos(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.__modelo = modelo
        self.__color = color
        self.__motor = motor
        self.__numero_puertas = numero_puertas
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__tipo_combustible = tipo_combustible

    #*********** Métodos generales (Polimorfismo) *************
    def arranque(self):
        print(f"El {self.__modelo} enciende su motor de forma estándar.")

    def apagado(self):
        print(f"El {self.__modelo} apaga su motor normalmente.")

    def aceleracion_frenado(self):
        print(f"El {self.__modelo} acelera y frena de forma estándar.")

    def sistema_direccion(self):
        print(f"El {self.__modelo} cuenta con dirección mecánica básica.")

    def climatizacion(self):
        print(f"El {self.__modelo} tiene ventilación estándar.")

    def tipo_seguridad(self):
        print(f"El {self.__modelo} cuenta con cinturones de seguridad básicos.")

    def luces(self):
        print(f"El {self.__modelo} enciende sus luces delanteras y traseras.")

    def sistema_ventanas(self):
        print(f"El {self.__modelo} tiene ventanas manuales.")

    def sistema_espejo(self):
        print(f"El {self.__modelo} tiene espejos manuales.")

    def mostrar_info(self):
        print("-" * 50)
        print(f"Modelo               : {self.__modelo}")
        print(f"Color                : {self.__color}")
        print(f"Motor                : {self.__motor}")
        print(f"Número de puertas    : {self.__numero_puertas}")
        print(f"Capacidad pasajeros  : {self.__capacidad_pasajeros}")
        print(f"Tipo de combustible  : {self.__tipo_combustible}")


    #************** Clases Hijas ****************

class CarroDeportivo(Carros):
    def __init__(self):
        super().__init__()
        super().asignar_datos("BMW Z4 Convertible", "Negro", "V6 Turbo 3.0L", 2, 2, "Gasolina")

    def arranque(self):
        print(f"El {self.get_modelo()} enciende con botón de encendido y un rugido deportivo.")

    def aceleracion_frenado(self):
        print(f"El {self.get_modelo()} acelera de 0 a 100 km/h en pocos segundos y frena con discos deportivos.")

    def sistema_direccion(self):
        print(f"El {self.get_modelo()} tiene dirección asistida deportiva de alta precisión.")

    def climatizacion(self):
        print(f"El {self.get_modelo()} cuenta con climatizador automático de dos zonas.")

    def tipo_seguridad(self):
        print(f"El {self.get_modelo()} tiene airbags múltiples y frenos ABS de alto rendimiento.")

    def sistema_ventanas(self):
        print(f"El {self.get_modelo()} tiene ventanas eléctricas y techo convertible.")


class Furgoneta(Carros):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Furgoneta de Carga", "Blanco", "Diésel 2.0L", 4, 3, "Diésel")

    def arranque(self):
        print(f"El {self.get_modelo()} enciende su motor diésel de forma robusta.")

    def aceleracion_frenado(self):
        print(f"El {self.get_modelo()} acelera de forma progresiva, pensado para carga.")

    def sistema_direccion(self):
        print(f"El {self.get_modelo()} tiene dirección asistida hidráulica para maniobrar con carga.")

    def climatizacion(self):
        print(f"El {self.get_modelo()} cuenta con aire acondicionado solo en la cabina del conductor.")

    def tipo_seguridad(self):
        print(f"El {self.get_modelo()} tiene sensores de reversa y alarma de retroceso.")

    def sistema_ventanas(self):
        print(f"El {self.get_modelo()} tiene ventanas eléctricas en la cabina delantera.")


class CamionRecolector(Carros):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Camión", "Blanco", "Diésel 6.0L", 2, 3, "Diésel")

    def arranque(self):
        print(f"El {self.get_modelo()} enciende su motor pesado con un sonido potente.")

    def aceleracion_frenado(self):
        print(f"El {self.get_modelo()} acelera lentamente por su peso y usa frenos de aire reforzados.")

    def sistema_direccion(self):
        print(f"El {self.get_modelo()} tiene dirección hidráulica reforzada para cargas pesadas.")

    def climatizacion(self):
        print(f"El {self.get_modelo()} cuenta con ventilación básica en la cabina.")

    def tipo_seguridad(self):
        print(f"El {self.get_modelo()} tiene luces de advertencia y alarma sonora de maniobra.")

    def luces(self):
        print(f"El {self.get_modelo()} enciende luces intermitentes de advertencia además de las normales.")


    #*************** Código Principal ***************
if __name__ == "__main__":
    carros = [CarroDeportivo(), Furgoneta(), CamionRecolector()]

    for carro in carros:
        carro.mostrar_info()
        carro.arranque()
        carro.apagado()
        carro.aceleracion_frenado()
        carro.sistema_direccion()
        carro.climatizacion()
        carro.tipo_seguridad()
        carro.luces()
        carro.sistema_ventanas()
        carro.sistema_espejo()
        print()