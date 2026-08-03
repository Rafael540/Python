"""
Argumentos nomeados e não nomeados em funções em Python
Argummento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Refatorar: editar o seu código.
"""


def soma(x , y, z=0):
    #Definição
    print(f'{x=}  y={y} {z=}','|','x + y + s =', x + y + z )

soma(1, 2, 3)
soma(2, 1, z=5)
soma(100, 200, 300)
