numero_secreto = 32
palpite = 0
while numero_secreto != palpite:
  palpite = int(input("informe um palpite:"))
  if palpite == numero_secreto:
    print("acertou")
  elif palpite > numero_secreto:
    print("chute um numero menor!")
  elif palpite < numero_secreto:
    print("Chute um numero maior!")
  else:
    print("Caso padrão")
