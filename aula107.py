# Exercício - unir listas
# Crie uma função zipper(como zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores de menor lista.
# ex:['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']


#def zipper():
#    for estado, sigla in zip(estados, siglas):
#        print (f'Estado= {estado} : Sigla = {sigla}')

#zipper()

#def zipper(lista1, lista2):
#   intervalo_maximo = min(len(lista1), len(lista2))
#   return [ (lista1 [i], lista2[i])for i in range(intervalo_maximo)]


#print(zipper(estados, siglas))
from itertools import zip_longest
print(list(zip(estados, siglas)))
print(list(zip_longest(estados, siglas, fillvalue='SEM CIDADE')))