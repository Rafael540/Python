"""
enumerate =
"""

lista = ['Maria', 'João', 'José']
lista.append('Rafael')

lista_enumerada = list(enumerate(lista))


#for item in lista_enumerada:
 #   indice ,nome = item
  #  print(indice, nome)

#for indice, nome in enumerate(lista):
#       print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'{valor}')