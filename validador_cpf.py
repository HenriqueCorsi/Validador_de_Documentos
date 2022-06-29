def validador_cpf(cpf):
    cpf = str(cpf)  # fazendo uma possivel conversão de Inteiro para String

    # Primeira Etapa -> Verifica se o tamanho do CPF está correto
    if len(cpf) == 11:
        cpf_parcial = cpf[:9]

        # Segunda Etapa -> Verifica se os dois ultimos digitos corresponde ao cpf
        # Verificando o primeiro digito
        soma = 0
        array_ = 0

        for index in range(10, 1, -1):
            soma = soma + index * int(cpf_parcial[array_])
            array_ = array_ + 1

        primeiro_digito = 11 - soma % 11

        if primeiro_digito > 9:
            primeiro_digito = 0
            cpf_parcial = cpf_parcial + str(primeiro_digito)
        else:
            cpf_parcial = cpf_parcial + str(primeiro_digito)

        # Verificando o segundo digito
        soma = 0
        array_ = 0

        for index in range(11, 1, -1):
            soma = soma + index * int(cpf_parcial[array_])
            array_ = array_ + 1

        segundo_digito = 11 - soma % 11

        if segundo_digito > 9:
            segundo_digito = 0
            cpf_parcial = cpf_parcial + str(segundo_digito)
        else:
            cpf_parcial = cpf_parcial + str(segundo_digito)

        sequencia = cpf_parcial == str(cpf_parcial[0]) * len(cpf)  # Terceira Etapa -> Evita sequencias como 1111111111

        if cpf == cpf_parcial and not sequencia: # Terceira Validação entra neste If
            print('-------------------------------')
            print('CPF Válido')
            fatia_um = cpf[:3]
            fatia_dois = cpf[3:6]
            fatia_tres = cpf[6:9]
            fatia_quatro = cpf[9:]
            print(f'CPF -> {fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}')
            print('-------------------------------')
        # Segunda ou Terceira Etapa -> falhou entra neste else abaixo
        else:
            print('-------------------------------')
            print('CPF Inválido')
            print('-------------------------------')

    # Primeira Etapa -> falhou entra neste else abaixo
    else:
        print('CPF Inválido. Verifique o número de caracteres que foi digitado!')


