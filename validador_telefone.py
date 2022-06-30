import re

def validador_telefone(telefone):
    telefone = str(telefone)

    padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
    val = re.search(padrao, telefone)
    if val:
        tel_formatado = f'+{val.group(1)} ({val.group(2)}) {val.group(3)}-{val.group(4)}'
        print(f' O número de telefone {tel_formatado} é valido ')
    else:
        print('Número de telefone invalido')

    

    