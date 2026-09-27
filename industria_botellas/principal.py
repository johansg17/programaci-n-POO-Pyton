#************* Código Principal - Ejercicio Botellas ***************

from botella_plastica import BotellaPlastica
from botella_vidrio import BotellaVidrio

if __name__ == "__main__":
    botella_plastica = BotellaPlastica()
    botella_vidrio = BotellaVidrio()

    botellas = [botella_plastica, botella_vidrio]

    for botella in botellas:
        botella.mostrar_info()
        botella.contener_liquidos()
        botella.facilitar_vertido()
        botella.cierre_hermetico()
        botella.transporte()
        botella.manejo()
        botella.compatibilidad_bebidas()
        botella.reutilizacion()
        botella.transparencia()
        print()