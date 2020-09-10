#ler todos os nomes que o usuário digitar até que ele não
#deseje continuar, exibir nomes em ordem alfabética
nomes = []

#Cria uma repetição que pergunta se o usuário deseja continuar
continuar = True

while continuar == True:
  nome = input("infome um nome:")
  #Coloca o nome no final da lista
  nomes.append(nome)
#Exibe a parcial da listacom os nomes
print(nomes)
if input("Deseja continuar (s/n)?") == "s":
  continuar = True
else:
   continuar = False
