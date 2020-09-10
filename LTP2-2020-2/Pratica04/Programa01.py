temperaturas = []

print(temperaturas)

contador = 0
while contador < 5:
  temperatura = float(input("informe uma temperatura"))
  #Adiciona temperatura no final
  temperaturas.append(temperatura)
  #Mostra o comportamento da lista entre as interações
  print(temperaturas)
  contador+= 1 #contador = contador + 1
