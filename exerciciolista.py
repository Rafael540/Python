"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserirm apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
"""

lista_compras = []

print('Selecione uma opção')
opcao = str(input('[i]nserir [a]pagar [l]istar [s]air: '))
while opcao != 's':
    match opcao:
        case 'i':
            item = str(input('Qual item você deseja inserir: '))
            lista_compras.append(item)
            opcao = str(input('[i]nserir [a]pagar [l]istar [s]air: '))

        case 'a':
            item = int(input('Escolha o indice para apagar: '))
            if item < 0 or item >=len(lista_compras):
                print('Esse indice não existe na lista')
            elif lista_compras[item] == '' or lista_compras[item] is None:
                print('Não existe nada ali(está vazio)')
            else:            
                del lista_compras[item]
                opcao = str(input('[i]nserir [a]pagar [l]istar [s]air: '))

        case 'l':
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
            opcao = str(input('[i]nserir [a]pagar [l]istar [s]air: '))

        case _:
            print('Opcao desconhecida')
            opcao = str(input('[i]nserir [a]pagar [l]istar [s]air: '))
print('O programa foi encerrado!')




