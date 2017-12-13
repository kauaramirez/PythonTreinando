# Tupla = Lista fixa, não tem como alterar e remover.
# Posso criar uma Tupla sem () apenas separando por ,.
semana = ("segunda","terça","quarta","quinta","sexta")
fds = ("sabado","domingo")

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
