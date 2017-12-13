# Para colocar 2 elementaos na agenda é preciso colocar [].
agenda = {
   "Kauã": ["555-000", "666-000"],
   "Natalia": "555-555",
    "Berenice": "555-222"
}

# Para acrescentar mais valores, como e-mail é preciso
# criar chave dentro de chave{{ }}.
agenda = {
    "Kauã":{
        "Telefone":["555-000", "666-000"],
        "Email": "kaua@kaua.com"
    },
    "Natalia":{
        "Telefone":"555-555"
    },
    "Berenice":{
        "Telefone":"555-222",
        "Email": "bere@bere.com"
    }
}

#Buscando o telefone do Kauã e E-mail Bere.
telKaua = agenda["Kauã"]["Telefone"]
emailNatalia = agenda["Berenice"]["Email"]

print(telKaua)
print(emailNatalia)
