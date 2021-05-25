class CalcularTax:
    def __init__(self, pesos):
        self._pesos = pesos

    @property
    def pesos(self):
        return self._pesos

    @pesos.setter
    def pesos(self, pesos):
        self._pesos = pesos

    def __str__(self):
        return f'Usted depositó ${self._pesos} pesos'


class DolarOficial:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        self._valor = valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def __str__(self):
        return f'El valor del dolar oficial es, ${self._valor}'

class RecargoArg:
    def __init__(self, imp):
        self._imp = imp

    @property
    def imp(self):
        return self._imp

    @imp.setter
    def imp(self, imp):
        self._imp = imp
        
    def recargoImp(self):
        return self._valor * self._imp
    
