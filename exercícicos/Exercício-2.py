n = int(input("Digite o número a verificar se existe na sequência de fibonacci: "))

a1 = 0
a2 = 1
resposta = False
if n == a1 or n == a2:
  resposta = True
else:
  while a2 < n:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    if a1 == n or a2 == n or a3 == n:
      resposta = True
      break
if resposta:
  print(f"O número {n} pertence à sequência!")
else:
  print(f"O número {n} não pertence a sequência!")