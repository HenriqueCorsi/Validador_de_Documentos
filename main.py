from validador_cpf import *
from validador_cnpj import *
from validador_telefone import *
from menu import *


menu()
select_user = int(input())
print('-------------------------------')
if select_user == 1:  # CPF
    cpf = input('Digite o CPF que gostaria de verificar: ')
    validador_cpf(cpf)
elif select_user == 2:  # CNPJ
    cnpj = input('Digite o CNPJ que gostaria de verificar: ')
    validador_cnpj(cnpj)
elif select_user == 3:  # TELEFONE
    telefone = input('Digite o TELEFONE que gostaria de verificar: ')
    validador_telefone(telefone)
elif select_user == 4:  # CEP
    pass
elif select_user == 5:
    print('Até logo...')
else:
    print('Opção Inválida')

