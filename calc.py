#!/usr/bin/python3
# -*- coding: utf-8 -*-
import calcoohija as ch


if __name__ == "__main__":
    if(len(ch.sys.argv) == 4):
        try:
            operando1 = int(ch.sys.argv[1])
            operando2 = int(ch.sys.argv[3])
        except ValueError:
            ch.sys.exit("Error: Non numerical parameters")

	op = ch.CalculadoraHija()

        if ch.sys.argv[2] == "suma":
            result = op.plus(operando1, operando2)
        elif ch.sys.argv[2] == "resta":
            result = op.minus(operando1, operando2)
        elif ch.sys.argv[2] == "multiplica":
            result = op.mult(operando1, operando2)
        elif ch.sys.argv[2] == "divide":
            result = op.div(operando1, operando2)
        else:
            ch.sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

        print(result)
    else:
        print("Introduzca dos operandos y un operador")
