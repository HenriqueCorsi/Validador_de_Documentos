def validador_cnpj(cnpj):
    cnpj = str(cnpj)

    # Primeira Etapa -> verificar se tem todos os caracteres
    if len(cnpj) == 14:
        cnpj_parcial = cnpj[:12]

        # Segunda Etapa -> Verifica se os dois ultimos digitos corresponde ao cnpj

        # Verificando o primeiro digito
        soma1 = 0
        index1 = 0
        for loop in range(5, 1, -1):
            soma1 = soma1 + loop * int(cnpj_parcial[index1])
            index1 = index1 + 1

        soma2 = 0
        for loop in range(9, 1, -1):
            soma2 = soma2 + loop * int(cnpj_parcial[index1])
            index1 = index1 + 1

        primeiro_digito = soma1 + soma2

        if 11 - primeiro_digito % 11 > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = 11 - primeiro_digito % 11

        # Verificando o segundo digito
        soma3 = 0
        index2 = 0
        for loop in range(6, 1, -1):
            soma3 = soma3 + loop * int(cnpj_parcial[index2])
            index2 = index2 + 1

        soma4 = 0
        for loop in range(9, 2, -1):
            soma4 = soma4 + loop * int(cnpj_parcial[index2])
            index2 = index2 + 1

        segundo_digito = primeiro_digito * 2 + soma3 + soma4

        if 11 - segundo_digito % 11 > 9:
            segundo_digito = 0
        else:
            segundo_digito = 11 - segundo_digito % 11

        cnpj_parcial = cnpj_parcial + str(primeiro_digito) + str(segundo_digito)

        # Terceira Etapa -> evita caractres sequencias como 11111111111
        sequencia = cnpj_parcial == str(cnpj_parcial[0] * len(cnpj))

        if cnpj == cnpj_parcial and not sequencia:
            print('-------------------------------')
            print('CNPJ Válido')
            fatia_um = cnpj[:2]
            fatia_dois = cnpj[2:5]
            fatia_tres = cnpj[5:8]
            fatia_quatro = cnpj[8:12]
            fatia_cinco = cnpj[12:]
            print(f'CNPJ -> {fatia_um}.{fatia_dois}.{fatia_tres}/{fatia_quatro}-{fatia_cinco}')
            print('-------------------------------')
        else:
            print('-------------------------------')
            print('CNPJ Inválido')
            print('-------------------------------')


    else:
        print('CNPJ Inválido. Digite o númeoro correto de caractres!')