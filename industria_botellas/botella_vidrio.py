#*********** Clase Hija - Botella de Vidrio ***************

from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Vidrio", 750, "Alargada tipo vino", "Diseño elegante y clásico", "Corcho", "Grabado del viñedo")

    def contener_liquidos(self):
        print(f"La botella de {self.get_material()} contiene líquidos como vino o bebidas de mayor valor.")

    def facilitar_vertido(self):
        print("Su cuello alargado permite un vertido lento y elegante.")

    def cierre_hermetico(self):
        print("El corcho asegura un cierre hermético que conserva mejor el líquido.")

    def transporte(self):
        print("Debe transportarse con cuidado, ya que es pesada y frágil.")

    def manejo(self):
        print("Requiere un manejo delicado para evitar que se rompa.")

    def compatibilidad_bebidas(self):
        print("Es compatible tanto con bebidas frías como calientes.")

    def reutilizacion(self):
        print("Se puede reutilizar muchas veces e incluso lavar sin perder calidad.")

    def transparencia(self):
        print("Tiene alta transparencia, permite ver el líquido con total claridad.")