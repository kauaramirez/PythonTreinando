# From Media = Importar o nomer do Arquivo Desejado.
# Import calcula_media = Importar a função Desejada.
from media import calcula_media

def test_media():
    assert calcula_media ([1,2,3]) == 2
    assert calcula_media ([2,2]) == 2
    assert calcula_media ([3,3,3]) == 3
