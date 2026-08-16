# raise - lanãndo exceções (erros)
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
     tipo_n = type(n)
     if not isinstance(n, (float, int)):
            raise TypeError(
                f'"{n}" dever ser int ou float.'
                f'{tipo_n.__name__} enviado'
            )
     return True

def deve_ser_int_ou_float(d):
    tipo_n = type(d)
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'"{d}" dever ser int ou float.'
            f'{tipo_n} enviado'
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d
    

print(divide(8, 0))