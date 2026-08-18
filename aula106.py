# Decoradores com parâmetros
# Decoradores server para criar funções

   
def parametro_decorador(nome):
    def fabrica_funcoes(func):
        print('Decoradora 1', nome)
        
        def aninhada(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final 
        return aninhada
    return fabrica_funcoes

@parametro_decorador(nome='primeiro')
@parametro_decorador(nome='segunda')
def soma(x,y):
    return x + y


dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)