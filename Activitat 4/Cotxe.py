class Cotxe:
    
    def __init__(self, marca, model, any, color, preu):
        self._marca = marca
        self._model = model
        self._any = any
        self._color = color
        self._preu = preu

    def get_marca(self):
        return self._marca

    def get_model(self):
        return self._model

    def get_any(self):
        return self._any

    def get_color(self):
        return self._color

    def get_preu(self):
        return self._preu

    def set_marca(self, marca):
        self._marca = marca

    def set_model(self, model):
        self._model = model

    def set_any(self, any):
        self._any = any

    def set_color(self, color):
        self._color = color

    def set_preu(self, preu):
        self._preu = preu
