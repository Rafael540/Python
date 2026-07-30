"""
Introdução às funções (def) em python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada)

Parametros podem ser variavéis

"""
#def Print(a , b ,c):
 #   print('Várias1')
  #  print('Varias2')
   # print

#def imprimir(a , b ,c):
#    print(a, b, c)

#imprimir(1,2,3)
#imprimir(4,5,6)

def saudacao(nome='Sem nome'):
    print(f'Olá,{nome}')

saudacao('Luiz Otávio')
saudacao('Rafael')
saudacao('Helena')
saudacao()