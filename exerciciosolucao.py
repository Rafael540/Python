lista = []

while True:
    print('Seleciona uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input ('Valor: ')
        lista.append(valor)
    elif opcao =='a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro!')
        except IndexError:
            print('Indice não existe na lista!')


    elif opcao == 'l':

        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')