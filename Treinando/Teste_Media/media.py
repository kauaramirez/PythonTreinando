# Escreva uma função que receba uma lista de numeros.
# e retorne a média dos numeros dessa lista.
# [1, 2, 3] => 2
# [5, 5, 4, 4] => 9

# crie um modulo para testar a função que.
# calcular a média.


# Coloquei soma = 0, pois vou ir acrescentando dados a essa variavel, para ir somando.
# Estou pegando valores da lista e atribuindo na minha variável "e".
# t = len(lista), t está recendo a quantidade de numeros totais na lista ex: 1,2,3 o len verifica que tem 3 numeros.

def calcula_media (lista):
    soma = 0
    for e in lista:
        soma = soma + e
    t = len(lista)
    return soma / t
