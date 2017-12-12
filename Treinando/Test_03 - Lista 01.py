# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8

def soma_dobro(a, b):
  soma = a + b
  if a == b:
    soma = soma * 2
  return soma

def test_ex03():
  print ('Soma dobro')
  assert soma_dobro(1, 2)  == 3
  assert soma_dobro(3, 2)  == 5
  assert soma_dobro(2, 2)  == 8
  assert soma_dobro(-1, 0) == -1
  assert soma_dobro(0, 0)  == 0
  assert soma_dobro(0, 1)  == 1
