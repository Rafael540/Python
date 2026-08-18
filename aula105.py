# Funções decoradoras e decoradores
# Decorar = Adcionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o python
# usar as funções decoradoras em outras funções
# Decoradores no Python são Syntax Sugar( Açúcar sntático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        resultado += 'Qualquer coisas'
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao #syntax sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if  not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


#inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('Luiz')
print(invertida)