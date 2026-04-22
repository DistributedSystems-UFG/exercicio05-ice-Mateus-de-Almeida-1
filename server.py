# Realizando o seguinte: acrescente novas funções no objeto servidor existente
import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):

    # Função original
    def printString(self, s, current=None):
        print(s)
    
    # NOVO: converte para maiúscula e imprime
    def printUpperCase(self, s, current=None):
        print(s.upper())
    
    # NOVO: conta e retorna o número de caracteres
    def countChars(self, s, current=None):
        return len(s)

# --- NOVO objeto Calculator ---
class CalculatorI(Demo.Calculator):

    def add(self, a, b, current=None):
        return a + b

    def subtract(self, a, b, current=None):
        return a - b

    def multiply(self, a, b, current=None):
        return a * b


communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))

# Registra o Calculator com a identidade "SimpleCalculator"
# NOVO: segundo objeto no mesmo servidor
calculator = CalculatorI()
adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()