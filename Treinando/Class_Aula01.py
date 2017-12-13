class Animal():
    
    def comer(self, comida):
        print(self.nome + " Comendo" + comida)

animal1 = Animal()
animal1.nome = "Pantera"
animal1.cor = "Preto"

animal1.comer(" carne")

animal2 = Animal()
animal2.nome = "Leão"
animal2.cor = "Laranja"
animal2.tipo = "Doidao"

animal2.comer(" carne")

#Sobrepoem.
animal3 = animal2
animal3.nome = "Arara"


print(animal1.nome)
print(animal1.cor)
print(animal2.nome)
print(animal2.cor)
print(animal2.tipo)
print(animal2.nome)
print(animal3.nome)
