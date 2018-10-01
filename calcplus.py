#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import calcoohija as ch

f = open(sys.argv[1])
for line in f:
    terminos = line.split(",")
    operador = terminos[0]
    operandos = terminos[2:]
    primernum = int(terminos[1])

    op = ch.CalculadoraHija()

    if operador == "suma":
        for elem in operandos:
            primernum = op.plus(primernum, int(elem))
            rsuma = primernum
        print(rsuma)

    elif operador == "resta":
        for elem in operandos:
            primernum = op.minus(primernum, int(elem))
            rresta = primernum
        print(rresta)

    elif operador == "multiplica":
        for elem in operandos:
            primernum = op.mult(primernum, int(elem))
            rmult = primernum
        print(rmult)

    elif operador == "divide":
        for elem in operandos:
            primernum = op.div(primernum, int(elem))
            rdiv = primernum
        print(rdiv)

    else:
        print("ERROR: Sólo puede sumar, restar, multiplicar o dividir.")
