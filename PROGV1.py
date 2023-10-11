import unicodedata

def remover_acentos(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

with open('b1.txt', 'r', encoding='utf-8') as arquivo:
    bairros = arquivo.readlines()

bairros_limpos = list(set(remover_acentos(bairro.strip().upper()) for bairro in bairros))

bairros_ordenados = sorted(bairros_limpos)

with open('bairros.txt', 'w', encoding='utf-8') as arquivo_saida:
    for bairro in bairros_ordenados:
        arquivo_saida.write(f"{bairro}\n")

print("Lista de bairros salva em 'bairros.txt'.")
