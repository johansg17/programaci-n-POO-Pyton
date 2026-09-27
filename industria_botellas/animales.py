    #************* Ejercicio POO - Animales **************

class Animal:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__habitat = ""
        self.__dieta = ""
        self.__tamano = ""
        self.__color = ""

    #************** Encapsulamiento: Getters y Setters ***************
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_habitat(self):
        return self.__habitat

    def set_habitat(self, habitat):
        self.__habitat = habitat

    def get_dieta(self):
        return self.__dieta

    def set_dieta(self, dieta):
        self.__dieta = dieta

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, tamano):
        self.__tamano = tamano

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def asignar_datos(self, nombre, edad, habitat, dieta, tamano, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__dieta = dieta
        self.__tamano = tamano
        self.__color = color

    #**************** Métodos generales (Polimorfismo) ***************
    def moverse(self):
        print(f"{self.__nombre} se mueve de forma general.")

    def comunicacion(self):
        print(f"{self.__nombre} se comunica de forma general.")

    def reproduccion(self):
        print(f"{self.__nombre} se reproduce de forma general.")

    def alimentarse(self):
        print(f"{self.__nombre} se alimenta de: {self.__dieta}.")

    def adaptacion(self):
        print(f"{self.__nombre} se adapta a su hábitat: {self.__habitat}.")

    def instintos(self):
        print(f"{self.__nombre} actúa guiado por su instinto.")

    def descanso(self):
        print(f"{self.__nombre} descansa cuando lo necesita.")

    def sueno(self):
        print(f"{self.__nombre} duerme para recuperar energía.")

    def interaccion_social(self):
        print(f"{self.__nombre} interactúa con otros animales de su especie.")

    def mostrar_info(self):
        print("-" * 45)
        print(f"Nombre : {self.__nombre}")
        print(f"Edad   : {self.__edad} años")
        print(f"Hábitat: {self.__habitat}")
        print(f"Dieta  : {self.__dieta}")
        print(f"Tamaño : {self.__tamano}")
        print(f"Color  : {self.__color}")


    #*************** Clases Hijas *****************

class Caballo(Animal):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Caballo", 5, "Pradera", "Herbívoro (pasto y avena)", "Grande", "Marrón")

    def moverse(self):
        print(f"{self.get_nombre()} se mueve galopando y trotando con sus 4 patas.")

    def comunicacion(self):
        print(f"{self.get_nombre()} se comunica mediante relinchos y el movimiento de sus orejas.")

    def reproduccion(self):
        print(f"{self.get_nombre()} es vivíparo, la yegua gesta al potrillo por varios meses.")

    def instintos(self):
        print(f"{self.get_nombre()} tiene instinto de manada y huye rápido ante el peligro.")


class Hipopotamo(Animal):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Hipopótamo", 12, "Ríos y pantanos", "Herbívoro (pasto acuático)", "Muy grande", "Gris")

    def moverse(self):
        print(f"{self.get_nombre()} camina por el fondo del río y nada sumergiendo su cuerpo.")

    def comunicacion(self):
        print(f"{self.get_nombre()} se comunica con bramidos y gruñidos muy fuertes.")

    def reproduccion(self):
        print(f"{self.get_nombre()} es vivíparo, la cría nace dentro del agua.")

    def adaptacion(self):
        print(f"{self.get_nombre()} tiene la piel adaptada para mantenerse húmeda fuera del agua.")


class Pez(Animal):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Pez", 2, "Acuario / Arrecife", "Omnívoro (algas y microorganismos)", "Pequeño", "Multicolor")

    def moverse(self):
        print(f"{self.get_nombre()} se mueve nadando gracias a sus aletas y su cola.")

    def comunicacion(self):
        print(f"{self.get_nombre()} se comunica mediante cambios de color y señales corporales.")

    def reproduccion(self):
        print(f"{self.get_nombre()} es ovíparo, pone huevos en el agua.")

    def adaptacion(self):
        print(f"{self.get_nombre()} respira mediante branquias, adaptado a la vida acuática.")


class Escarabajo(Animal):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Escarabajo", 1, "Bosque / Suelo", "Detritívoro (materia orgánica)", "Pequeño", "Negro brillante")

    def moverse(self):
        print(f"{self.get_nombre()} camina con sus 6 patas y también puede volar cortas distancias.")

    def comunicacion(self):
        print(f"{self.get_nombre()} se comunica mediante feromonas y vibraciones.")

    def reproduccion(self):
        print(f"{self.get_nombre()} es ovíparo, pasa por metamorfosis (huevo, larva, pupa, adulto).")

    def instintos(self):
        print(f"{self.get_nombre()} tiene instinto de defensa mostrando su exoesqueleto duro.")


class Pato(Animal):
    def __init__(self):
        super().__init__()
        super().asignar_datos("Pato", 3, "Lagos y humedales", "Omnívoro (plantas e insectos)", "Mediano", "Verde y café")

    def moverse(self):
        print(f"{self.get_nombre()} camina, nada con sus patas palmeadas y también vuela.")

    def comunicacion(self):
        print(f"{self.get_nombre()} se comunica emitiendo graznidos.")

    def reproduccion(self):
        print(f"{self.get_nombre()} es ovíparo, pone huevos en nidos cerca del agua.")

    def adaptacion(self):
        print(f"{self.get_nombre()} tiene plumas impermeables que le permiten flotar.")


    #**************** Código Principal *****************
if __name__ == "__main__":
    animales = [Caballo(), Hipopotamo(), Pez(), Escarabajo(), Pato()]

    for animal in animales:
        animal.mostrar_info()
        animal.moverse()
        animal.comunicacion()
        animal.reproduccion()
        animal.alimentarse()
        animal.adaptacion()
        animal.instintos()
        animal.descanso()
        animal.sueno()
        animal.interaccion_social()
        print()