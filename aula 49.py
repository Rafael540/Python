"""
Listas em python
Tipo list - mutável
Suporta vérios valores de qualquer tipo
Conhecimentos reutilizáveis - indíces e fatiamentos
Métodos úteis:
    append, insert, pop, del, clear, extend, +

    Create Read Update Delete
    Criar, ler, alterar, apagar = lista[i] CRUD

Dependendo do tamanho da lista, o tamanho dele requer muito processamento    
"""

lista = [10,20,30,40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50)
# ultimo_valor = lista.pop()
# lista.append(60)
# lista.append(70)
#ultimo_valor = lista.pop()
# print(lista, 'Removido', ultimo_valor)


lista = []
i = 0
vezes = int(input('Quantos vezes você quer inserir os números: '))

while i != vezes:
    n = int(input('Digite um núnero: '))
    lista.append(n)
    i += 1
print( "Terminou o looping!")

print(lista)

deletar = int(input(f'De 0 a {vezes}, digite qual indice deseja apagar: '))
del lista[deletar - 1]
print(lista)