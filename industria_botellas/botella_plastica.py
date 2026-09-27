#************* Clase Hija - Botella Plástica **************

from botella import Botella

class BotellaPlastica(Botella):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Plástico", 600, "Cilíndrica", "Ergonómico con curvas para agarre", "Rosca plástica", "Sin grabados")

    def contener_liquidos(self):
        print(f"La botella de {self.get_material()} contiene líquidos livianos como agua y gaseosas.")

    def facilitar_vertido(self):
        print("Su pico angosto facilita un vertido controlado y sin derrames.")

    def cierre_hermetico(self):
        print("La tapa de rosca plástica asegura un cierre hermético y seguro.")

    def transporte(self):
        print("Es liviana y resistente a golpes, ideal para transportar en cualquier lugar.")

    def manejo(self):
        print("Se puede manejar con facilidad, ya que es flexible y no se rompe fácilmente.")

    def compatibilidad_bebidas(self):
        print("Solo es compatible con bebidas frías o a temperatura ambiente.")

    def reutilizacion(self):
        print("Se puede reutilizar varias veces, aunque se recomienda reciclarla con el tiempo.")

    def transparencia(self):
        print("Es translúcida, permite ver el nivel de líquido pero no con total claridad.")