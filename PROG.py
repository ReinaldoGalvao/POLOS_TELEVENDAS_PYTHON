'''
PROGRAMA:
    COLOCA EM ORDEM ALFABETICA
    REMOVE ACENTOS E CEDILHAS
    REMOVE DUPLICIDADES EM NOMES
    REMOVE ESPAÇOS ANTES E DEPOIS DOS NOMES
'''
import unicodedata

def remover_acentos(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

with open('b1.txt', 'r', encoding='utf-8') as arquivo:
    bairros = arquivo.readlines()

bairros_limpos = [remover_acentos(bairro.strip().upper()) for bairro in bairros]

bairros_unicos_ordenados = sorted(set(bairros_limpos))

with open('bairros.txt', 'w', encoding='utf-8') as arquivo_saida:
    for bairro in bairros_unicos_ordenados:
        arquivo_saida.write(f"{bairro}\n")

print(f"Foram encontrados {len(bairros_limpos) - len(bairros_unicos_ordenados)} bairros duplicados.")
print("Lista de bairros salva em 'bairros.txt'.")
