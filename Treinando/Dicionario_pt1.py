# Primeiro valor dentro do Dicionario é chamando de Chave.
# : Estou atribuindo a chave a algum valor no caso Kauã Ramires ou Natalia Nadgela.
#item1 = dic ['1700652'] = Estou buscando o valor linkado a essa Chave.

alunos = {'1700652': 'Kauã Ramires','1700653': 'Natalia Nadgela'}
aluno = {'nome': "Kauã Ramires", "idade": "26"}
agenda = {'Igor': "555-555", "Jorge": "555-666"}

#Printando valores Chaves.
print(alunos["1700652"])
print(aluno["idade"])

# Alterando items no Dicionario.
alunos ["1700652"] = "Nataka"
aluno ["idade"] = "25"
agenda ["Jorge"] = "555-690"

#Atribuindo novos valores ao Dicionario.
alunos["333333"] = "Carlos"
aluno["sexo"] = "M"

#Printando 2 valores juntos.
print(alunos["333333"], aluno["sexo"])

#Printando todo o Dicionario.
print(alunos)
print(aluno)
print(agenda)

#Para descobrir o tamanho do dicionario é só.
tamAluno = len(aluno)
tamAlunos = len(alunos)
tamAgenda = len(agenda)

print(tamAluno, tamAlunos, tamAgenda)

#Removendo um contato da agenda.
del agenda['Igor']
print(agenda)

#in = Verificar se possui algum item no Dicionario - No caso o Jorge.
existe = "Jorge" in agenda
print(existe)
existe = 'Igor' in agenda
print(existe)

# keys = Pegar todas as chaves do dicionario solicitado.
chaves = alunos.keys()
print(chaves)

# values = Pegar todos os valores de um dicionario solicitado.
valores = alunos.values()
print(valores)

# items = Retorna uma lista(Dicionario) em formato de tupla.
items = alunos.items()
print(items)

# Percorrendo uma tupla em python.
for chave, valor in alunos.items():
    print(chave)
    print(valor)
