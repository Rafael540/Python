# Modulos padrão do Python(import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens : nomes grandes
import sys

#platform = 'A MINHA'
#print(sys.platform)
#print(platform)

from sys import exit, platform

print(platform)

# parte - from nome_modelo import objeto1, objeto2
# vantagens - nomes pequenos
# Desvantagens: Sem o namespace do módulo

# alias 1 - import nome_modulo de apelido
# alias 2 - from nome_modulo import objeto as apelido
# Vantagens; você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# Má prática - from nome_modelo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo