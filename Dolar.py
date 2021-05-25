from ClaseConversor import CalcularTax
from ClaseConversor import RecargoArg
from ClaseConversor import DolarOficial

class DolarArg(CalcularTax, RecargoArg, DolarOficial):
    def __init__(self, pesos, imp = 1.65, oficial = 94.22):
        CalcularTax.__init__(self, pesos)
        RecargoArg.__init__(self, imp)
        DolarOficial.__init__(self, oficial)

    def calcularCompra(self):
        return self._pesos / RecargoArg.recargoImp(self)

    def calcularTax(self):
        return DolarArg.calcularCompra(self) * self._valor

    def impuestoTotal(self):
        return  self._pesos - DolarArg.calcularTax(self)

    def __str__(self):
        return f'{CalcularTax.__str__(self)}, {DolarOficial.__str__(self)}, el Total en Dolares es ${DolarArg.calcularCompra(self):.2f}, se redujeron ${DolarArg.impuestoTotal(self):.2f} en impuestos'








