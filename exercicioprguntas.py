perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5+2?',
        'Opções' : ['25', '55', '10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4', '5', '2','1'],
        'Resposta': '5',
    },
        
]

valor = 0

print("Pergunta: ", perguntas[0]['Pergunta'])
print('Opções: ')
for indice, opcao in enumerate(perguntas[0]['Opções']):
    print(indice + 1,")",opcao)
pergunta_1 = str(input('Escolha uma opção: '))
if pergunta_1 == '4':
    try:
        print('Resposta correta!')
        valor += 1
    except(KeyError):
        print('Respota incorreta!')

print()
print("Pergunta: ", perguntas[1]['Pergunta'])
print('Opções: ')
for indice, opcao in enumerate(perguntas[1]['Opções']):
    print(indice + 1,")",opcao)
pergunta_1 = str(input('Escolha uma opção: '))
if pergunta_1 == '25':
    try:
        print('Resposta correta!')
        valor += 1
    except(KeyError):
        print('Respota incorreta!')
 
print()
print("Pergunta: ", perguntas[2]['Pergunta'])
print('Opções: ')
for indice, opcao in enumerate(perguntas[2]['Opções']):
    print(indice + 1,")",opcao)
pergunta_1 = str(input('Escolha uma opção: '))
if pergunta_1 == '5':
    try:
        print('Resposta correta!')
        valor += 1
    except(KeyError):
         print('Respota incorreta!')

print()
print(f'Você acertou {valor}')
print('de 3 perguntas')
print()
