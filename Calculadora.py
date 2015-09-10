
# coding=utf-8
#Definimos las funciones que hara la calculadora

def Suma():
	""" Definimos la operacion suma """
	print "\nSUMA\n"
	numero1 = (int(input("Ingrese el valor 1: ")))
	numero2 = (int(input("Ingrese el valor 2: ")))
	print numero1+numero2

def Resta():
	""" Definimos la operacion resta """
	print "\nResta\n"
	numero1 = (int(input("Ingrese el valor 1: ")))
	numero2 = (int(input("Ingrese el valor 2: ")))
	print numero1-numero2

def Multi():
	""" Definimos la operacion multiplicacion """
	print "\nMultiplicacion\n"
	numero1 = (int(input("Ingrese el valor 1: ")))
	numero2 = (int(input("Ingrese el valor 2: ")))
	print numero1*numero2
	
def Division():
	""" Definimos la operacion division """
	print "\nDivision\n"
	numero1 = (int(input("Ingrese el valor 1: ")))
	numero2 = (int(input("Ingrese el valor 2: ")))
	if numero2>0:
		print numero1/numero2
	else:
		print "NO se puede dividir por 0"