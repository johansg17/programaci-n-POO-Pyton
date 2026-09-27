    #************* Clase Base - Botella *************

class Botella:
    def __init__(self):
        self.__material = ""
        self.__capacidad = 0
        self.__forma = ""
        self.__diseno = ""
        self.__tapa = ""
        self.__grabados = ""

    #*************** Getters *************
    def get_material(self):
        return self.__material

    def get_capacidad(self):
        return self.__capacidad

    def get_forma(self):
        return self.__forma

    def get_diseno(self):
        return self.__diseno

    def get_tapa(self):
        return self.__tapa

    def get_grabados(self):
        return self.__grabados

    #*************** Setters **************
    def set_material(self, material):
        self.__material = material

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def set_forma(self, forma):
        self.__forma = forma

    def set_diseno(self, diseno):
        self.__diseno = diseno

    def set_tapa(self, tapa):
        self.__tapa = tapa

    def set_grabados(self, grabados):
        self.__grabados = grabados

    def asignar_datos(self, material, capacidad, forma, diseno, tapa, grabados):
        self.__material = material
        self.__capacidad = capacidad
        self.__forma = forma
        self.__diseno = diseno
        self.__tapa = tapa
        self.__grabados = grabados

    #**************** Métodos generales (Polimorfismo) **************
    def contener_liquidos(self):
        print(f"La botella de {self.__material} contiene líquidos de forma general.")

    def facilitar_vertido(self):
        print("Facilita el vertido del líquido de forma estándar.")

    def cierre_hermetico(self):
        print(f"Cuenta con una tapa tipo {self.__tapa} para el cierre.")

    def transporte(self):
        print("Se puede transportar con un manejo normal.")

    def manejo(self):
        print("Requiere un manejo estándar para evitar daños.")

    def compatibilidad_bebidas(self):
        print("Es compatible con bebidas frías.")

    def reutilizacion(self):
        print("Puede reutilizarse de forma limitada.")

    def transparencia(self):
        print("Tiene un nivel de transparencia medio.")

    def mostrar_info(self):
        print("-" * 45)
        print(f"Material  : {self.__material}")
        print(f"Capacidad : {self.__capacidad} ml")
        print(f"Forma     : {self.__forma}")
        print(f"Diseño    : {self.__diseno}")
        print(f"Tapa      : {self.__tapa}")
        print(f"Grabados  : {self.__grabados}")