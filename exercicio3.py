# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou impoar


def multiplicar(*args):
    total = 1
    for numero in args:
         total *= numero
    return total

mulitplicação = multiplicar(1,2,3,4,5,6)
print(mulitplicação)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f"{numero} é par"
    else: 
        return f"{numero} é ímpar"

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))


#def multi(*args):
   # variavel = int(input('Quantos números você deseja inserir: '))
    #multiplicacao = 1
    #i = 0
    #soma = 0
    #for i in range(variavel):
     #   numero = int(input('Insira um número: '))
      #  multiplicacao = numero * multiplicacao
       # soma += multiplicacao
        #print(soma)
    #return multi()
#multi()

