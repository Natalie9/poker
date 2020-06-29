from collections import defaultdict


def transforma_valor(i):
    switcher = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    return switcher.get(i, i)


def transforma_valor_numerico(i):
    switcher = {
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A'
    }
    return switcher.get(i, i)


def ordena_valores(mao):
    return sorted(mao, key=lambda x: x['valor'])


def combina_naipe(mao):
    combined = defaultdict(list)
    for i in mao:
        combined[i['naipe']].append(i['valor'])
    return sorted(combined.items())


def combina_valor(mao):
    combined = defaultdict(list)
    for i in mao:
        combined[i['valor']].append(i['naipe'])
    return sorted(combined.items())


def verifica_quantidade_nipes(mao):
    return len(mao['cartas_naipe'])


def verifica_quantidade_valor(mao):
    return len(mao['cartas_valor'])


def verifica_regras(mao):
    # Royal Flush
    # maos que tem apenas um nipe
    if mao['qtd_nipes'] == 1:
        ##case Royal Flush
        if mao['cartas_naipe'][0][1] == [10, 11, 12, 13, 14]:
            mao['tipo_mao'] = 'Royal Flush'
            mao['posicao'] = 1


        ##case Straight Flush
        elif mao['cartas_naipe'][0][1][4] != 14:
            if mao['cartas_naipe'][0][1][0] + 4 == mao['cartas_naipe'][0][1][4]:
                mao['tipo_mao'] = 'Straight Flush'
                mao['posicao'] = 2
        elif mao['cartas_naipe'][0][1][4] == 14:
            mao['cartas_naipe'][0][1][4] = 1
            if mao['cartas_naipe'][0][1][0] + 4 == mao['cartas_naipe'][0][1][4]:
                mao['tipo_mao'] = 'Straight Flush'
                mao['posicao'] = 2


        ##case Flush
        else:
            mao['tipo_mao'] = 'Flush'
            mao['posicao'] = 5

    elif mao['qtd_valor'] == 2:
        ## Quadra
        if len(mao['cartas_valor'][0][1]) == 4 or len(mao['cartas_valor'][1][1]) == 4:
            mao['tipo_mao'] = 'Quadra'
            mao['posicao'] = 3

        else:
            mao['tipo_mao'] = 'Full House'
            mao['posicao'] = 4

    elif mao['qtd_valor'] == 3:
        if (len(mao['cartas_valor'][0][1]) == 3 or len(mao['cartas_valor'][1][1]) == 3 or len(
                mao['cartas_valor'][2][1]) == 3):
            mao['tipo_mao'] = 'Trinca'
            mao['posicao'] = 7
        else:
            mao['tipo_mao'] = 'Dois pares'
            mao['posicao'] = 8
    ## tendo 4 valores distintos em 5 cartas, existe pelo menos 1 valor em par
    elif mao['qtd_valor'] == 4:
        mao['tipo_mao'] = 'Par'
        mao['posicao'] = 9

    ##se não entrou em nenhuma regra por naipe e possui 5 valores distintos
    else:
        print('else')
        if mao['cartas_valor'][4][0] != 14 and mao['cartas_valor'][0][0] + 4 == mao['cartas_valor'][4][0]:
            mao['tipo_mao'] = 'Sequencia'
            mao['posicao'] = 6

        ##caso seja sequencia de 2 3 4 5 e A valendo 1
        elif mao['cartas_valor'][4][0] == 14 and mao['cartas_valor'][0][0] == 2 and mao['cartas_valor'][0][0] + 3 == \
                mao['cartas_valor'][3][0]:
            y = list(mao['cartas_valor'][4])
            y[0] = 1
            mao['cartas_valor'][4] = tuple(y)
            mao['tipo_mao'] = 'Sequencia'
            mao['posicao'] = 6

        ##sem naipes ou valores em comum/sequência
        else:
            mao['tipo_mao'] = 'Carta alta'
            mao['posicao'] = 10

    return mao


##TODO fazer verificação em caso de empate
## são muitos casos de empate, inviável concluir no prazo


def fazer_verficacao(mao):
    ##transoforma valores J Q K A em valores númericos respectivamente 11 12 13 1
    for i in mao:
        i['valor'] = int(transforma_valor(i['valor']))

    ##ordena valores
    mao = ordena_valores(mao)

    ##criando dicionarios com informações da mão
    mao_result = {}

    ##forma grupos por nipes
    mao_result['cartas_naipe'] = combina_naipe(mao)

    ##forma grupos por valor
    mao_result['cartas_valor'] = combina_valor(mao)

    ##verifica quantos nipes tem
    mao_result['qtd_nipes'] = verifica_quantidade_nipes(mao_result)

    ##verifica quantos valores distintos tem
    mao_result['qtd_valor'] = verifica_quantidade_valor(mao_result)

    ##consultando regras
    mao_result = verifica_regras(mao_result)

    ##transoforma valores 11 12 13 1 em valores respectivamente J Q K A
    for i in mao:
        i['valor'] = transforma_valor_numerico(i['valor'])

    for i in mao:
        print(i['naipe'], i['valor'])
    print(mao_result['tipo_mao'])
    print(str(mao_result['posicao']) + '° colocação')
    return mao_result


def desempate(mao1, mao2):
    regra = mao2['posicao']

    ## empate de royal flush ?

    ##Straight Flush
    if regra == 2:
        for i, item in enumerate(mao1['cartas_naipe'][0][1]):
            maior1 = mao1['cartas_naipe'][0][1][i]
            maior2 = mao2['cartas_naipe'][0][1][i]
            if maior1 > maior2:
                print("mao 1")
                return mao1
            elif maior2 > maior1:
                print("mao 2")
                return mao2
        print("empate total")

    if regra == 3:
        print('regra 3')
        ##determina quem é a quadra de cada mao
        if len(mao1['cartas_valor'][0][1]) == 4:
            quadra1 = mao1['cartas_valor'][0][0]
            kicker1 = mao1['cartas_valor'][1][0]
        else:
            quadra1 = mao1['cartas_valor'][1][0]
            kicker1 = mao1['cartas_valor'][0][0]

        if len(mao2['cartas_valor'][0][1]) == 4:
            quadra2 = mao2['cartas_valor'][0][0]
            kicker2 = mao2['cartas_valor'][1][0]
        else:
            quadra2 = mao2['cartas_valor'][1][0]
            kicker2 = mao2['cartas_valor'][0][0]

        if quadra1 > quadra2:
            return mao1

        elif quadra2 > quadra1:
            return mao2

        else:
            if kicker1 > kicker2:
                return mao1
            elif kicker2 > kicker1:
                return mao2
            else:
                print('empate total')


def compara_maos(mao1, mao2):
    import json
    if mao1['posicao'] < mao2['posicao']:
        maoT = {"title": "Mao 1", "vencedor": mao1, 'perdedor': mao2}
        return maoT

    elif mao2['posicao'] < mao1['posicao']:
        maoT = {"title": "Mao 2", "vencedor": mao2, 'perdedor': mao1}
        return maoT
    else:
        print('empate')
        return {"title": "Empate", "vencedor": mao2, 'perdedor': mao1}
