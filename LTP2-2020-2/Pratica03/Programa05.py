#Nossa calculadora
from os import system
from math import sin,cos,radians
#Cria uma função
def mostrar_menu():
  print('0 - Sair')
  print('+ - Somar')
  print('- - Subtrair')
  print('* - Multiplicar')
  print('/ - Dividir')
  print('sen - Seno')
  print('cos - Cosseno')
  print('elevado - Potência')
  print('raiz - Calcular a Raiz')

def somar():
  numero1 = float(input('Numero 1:'))
  numero2 = float(input('Numero 2:'))
  resultado = numero1 + numero2
  print('Resultado da soma:', resultado)

def subtrair():
  numero1 = float(input("Numero 1:"))
  numero2 = float(input("Numero 2:"))
  resultado = numero1 - numero2
  print("resultado da subtraçao", resultado)

def multiplicar():
  numero1 = float(input("Numero 1:"))
  numero2 = float(input("Numero 2:"))
  resultado = numero1 * numero2
  print("resultado da multiplicaçao", resultado)

def dividir():
  numero1 = float(input("Numero 1:"))
  numero2 = float(input("Numero 2:"))
  resultado = numero1 / numero2
  print("resultado da divizao", resultado)

def Potencia():
  base = float(input('base:'))
  resultado = base ** expoente
  print("resultado da potencia", resultado)

def seno():
  angulo = float(input("Angulo:"))
  print("Seno do angulo:", sin(radians(angulo)))

def cosseno():
  angulo = float(input("Angulo:"))
  print("cos do angulo:", cos(radians(angulo)))





ligado = True

while ligado == True:
  mostrar_menu()
  opcao = input('Opcao:')
  if opcao == '0':
    ligado = False
  elif opcao == '+':
    somar()
  elif opcao == '-':
    subtrair()
  elif opcao == '*':
    multiplicar()
  elif opcao == 'sen':
   seno()
  elif opcao == '/':
    dividir()
  elif opcao == 'elevado':
    potencia()
