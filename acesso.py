import re
try:
    REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def apenas_numeros(cnpj):
        return re.sub(r'[^0-9]', '', cnpj)

    def valida(cnpj):
        cnpj = apenas_numeros(cnpj)

        if eh_sequencia(cnpj):
            print(f'{cnpj}: É uma sequência!')
            return False

        novo_cnpj = calcula_digito(cnpj, digito=1)
        novo_cnpj = calcula_digito(novo_cnpj, digito=2)

        if novo_cnpj == cnpj:
            print(f'{cnpj} : Válido')
        else:
            print(f'{cnpj}: CNPJ inválido')
    def calcula_digito(cnpj, digito):
        if digito == 1:
            regressivos = REGRESSIVOS[1:]
            novo_cnpj = cnpj[:-2]
        elif digito == 2:
            regressivos = REGRESSIVOS
            novo_cnpj = cnpj
        else:
            return None

        total = 0
        for indice, regressivo in enumerate(regressivos):
            total += int(cnpj[indice]) * regressivo

        digito = 11 -(total%11)
        digito = digito if digito <= 9 else 0

        return f'{novo_cnpj}{digito}'

    def eh_sequencia(cnpj):
        sequencia = cnpj[0] * len(cnpj)

        if sequencia == cnpj:
            return True
        else:
            return False


except IndexError as e:
    print('Digite um CNPJ : ', e)

# 00.000.000/0000-00
cnpj1 = '68.556.349/0001-48'
valida(cnpj1)