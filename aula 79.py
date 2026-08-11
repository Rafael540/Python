# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)
