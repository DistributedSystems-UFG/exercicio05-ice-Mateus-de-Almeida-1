import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

# Função original
printer.printString("Hello World!")

# NOVO: Imprime em maiúscula
printer.printUpperCase("Hello World!")

# -- NOvo: conecta ao objeto Calculator
base_calc = communicator.stringToProxy("SimpleCalculator:default -p 11000")
calculator = Demo.CalculatorPrx.checkedCast(base_calc)

if not calculator:
    raise RuntimeError("Invalid proxy")

# NOVO: realiza operação soma
soma = calculator.add(5, 3)
print(f"Soma: {soma}")

# NOVO: realiza operação subtração
subtracao = calculator.subtract(5, 3)
print(f"Subtração: {subtracao}")

# NOVO: realiza operação multiplicação
multiplicacao = calculator.multiply(5, 3)
print(f"Multiplicação: {multiplicacao}")
