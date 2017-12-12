# upper(), transforma valores minuscula em Maiuscula.
# extend(), acrescenta mais de 1 valor para lista, append acrescenta apenas 1 valor por vez.
# count(), conta valores.
# or = ou --- elif = senaose -- and = e
# Para usar elif, precisa ter um if antes.

respostas = []

r1 = input('Telefonou para a vítima? (S/N): ').upper()
r2 = input('Esteve no local do crime? (S/N): ').upper()
r3 = input('Mora perto da vítima? (S/N): ').upper()
r4 = input('Devia para a vítima? (S/N): ').upper()
r5 = input('Já trabalhou com a vítima? (S/N): ').upper()

respostas.extend([r1, r2, r3, r4, r5])

#Estou contando quantas vezes o S aparece com count.
sim = respostas.count('S')

if sim == 2:
    print('Suspeito')
#elif sim > 2 and sim < 5:    
elif sim == 3 or sim == 4:
    print ('Cumplice')
elif sim == 5:
    print('Culpado')
else:
    print('Inocente')
