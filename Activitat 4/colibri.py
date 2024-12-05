class Colibri:
    def __init__(self, especie, tamaño, peso, color, habitat):
        self.__especie = especie
        self.__tamaño = tamaño
        self.__peso = peso
        self.__color = color
        self.__habitat = habitat

    def get_especie(self):
        return self.__especie

    def get_tamaño(self):
        return self.__tamaño

    def get_peso(self):
        return self.__peso

    def get_color(self):
        return self.__color

    def get_habitat(self):
        return self.__habitat

    def set_especie(self, especie):
        self.__especie = especie

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def set_peso(self, peso):
        self.__peso = peso

    def set_color(self, color):
        self.__color = color

    def set_habitat(self, habitat):
        self.__habitat = habitat