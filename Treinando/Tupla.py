# Tupla = Lista fixa, não tem como alterar e remover.
# Posso criar uma Tupla sem () apenas separando por ,.
semana = ("segunda","terça","quarta","quinta","sexta")
fds = ("sabado","domingo")

# Juntando 2 Tuplas.
dias = semana + fds
print(dias)

#Python entende que dia1 = sabado e dia2 = domingo.
dia1, dia2 = fds

# Quando for uma tupla de apenas um elemento, colocar uma
# virgula no final.
estudar = ("domingo",)

print(semana[1])
print(fds[0])
print(estudar[0])

#Contalizando quantidade.
tamanho = len(semana)
print(tamanho)

# Transformando Tupla em Lista.
semana = list(semana)

# Transformando uma lista em tupla.
lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

# Eu posso alterar uma lista[] dentro de uma tupla.
tupla = (0, [1,2])
tupla[1][0] = 5
print(tupla)
