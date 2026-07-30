"""
Lista de listas e seus indices
"""

salas = [
    #0
    ['Maria', 'Helena', ],

    ['Elaine', ],

    ['Luiz', 'Joao', 'Eduarda', (0, 10, 20 ,30, 40)],
]

#print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)