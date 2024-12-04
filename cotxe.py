class Coche:
    def __init__(self, marca, modelo, año_fabricacion, color, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__año_fabricacion = año_fabricacion
        self.__color = color
        self.__precio = precio

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año_fabricacion(self):
        return self.__año_fabricacion

    def get_color(self):
        return self.__color

    def get_precio(self):
        return self.__precio

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año_fabricacion(self, año_fabricacion):
        self.__año_fabricacion = año_fabricacion

    def set_color(self, color):
        self.__color = color

    def set_precio(self, precio):
        self.__precio = precio