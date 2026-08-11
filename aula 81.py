'''
Função Lambda em Python
A função lambda é uma função como qualquer
outra em Python. Porém,são funções anônimas
que contém uma linha, OU seja, tudo deve ser
contido dnetro de uma única expresão
lista = [
        {'nome' : 'Luiz', 'sobrenome': 'miranda'},
        {'nome' : 'Maria', 'sobrenome': 'Oliveira'},
        {'nome' : 'Daniel', 'sobrenome': 'Silva'},
        {'nome' : 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome' : 'Aline', 'sobrenome': 'Souza'},
        ]
'''
#lista = [4, 32, 1, 34, 2, 6 ,6 ,21,]
#lista.sort(reverse=True)


lista = [
        {'nome' : 'Luiz', 'sobrenome': 'miranda'},
        {'nome' : 'Maria', 'sobrenome': 'Oliveira'},
        {'nome' : 'Daniel', 'sobrenome': 'Silva'},
        {'nome' : 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome' : 'Aline', 'sobrenome': 'Souza'},
        ]

def exibir(lista):
    for item in lista:
        print(item)
    print()

    
l1 = sorted(lista , key=lambda item: item['nome'])
l2 = sorted(lista , key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)