#Determinar se um número inteiro é par ou impar
numero= int(input("numero:"))
#Calcula o resto da divisao de um numero por 2
resto = numero % 2

#condição
if resto == 0:
  print("PAR")
else:
  print("ímpar")
