"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados. 
Sempre que executada determinada ação com funcão, retorna determinado
valor

"""
# x = 1


#def escopo():
 #   global x 
  #  x = 10
   # def outra_funcao():
    #    y = 2
     #   print(x, y)

    #outra_funcao()
    #print(x)

#print(x)
#escopo()
#print(x)

def soma(x,y):
    if x >10:
        return 10, 20
    return x + y
    

#return significa que ira returnar alguma 
# coisa que será utilizado em variaveis
#print é um função que exibe nada na telas

soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma(11,55))
