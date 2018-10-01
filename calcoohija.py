import sys
from calcoo import Calculadora

class CalculadoraHija(Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed.")

