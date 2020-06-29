from teste import transforma_valor, combina_naipe, combina_valor, verifica_quantidade_nipes, verifica_quantidade_valor, \
    verifica_regras, ordena_valores, fazer_verficacao, compara_maos

## VALORES DE ENTRADA
# naipe  C E P O
# valores 2 3 4 5 6 7 8 9 10 J Q K A
## Royal Flush - Straight flush - Quadra - Full house - Flush - Sequência - Trinca - Dois Pares - Par - Nenhum par
mao1 = [
    {'naipe': 'C',
     'valor': '10'},
    {'naipe': 'C',
     'valor': 'J'},
    {'naipe': 'C',
     'valor': 'Q'},
    {'naipe': 'C',
     'valor': 'K'},
    {'naipe': 'C',
     'valor': 'A'}
]

mao2 = [
    {'naipe': 'C',
     'valor': '2'},
    {'naipe': 'C',
     'valor': '3'},
    {'naipe': 'C',
     'valor': '5'},
    {'naipe': 'C',
     'valor': '4'},
    {'naipe': 'C',
     'valor': '6'}
]

mao22 = [
    {'naipe': 'C',
     'valor': '2'},
    {'naipe': 'C',
     'valor': '3'},
    {'naipe': 'C',
     'valor': '5'},
    {'naipe': 'C',
     'valor': '4'},
    {'naipe': 'C',
     'valor': 'A'}
]

mao3 = [
    {'naipe': 'O',
     'valor': '10'},
    {'naipe': 'O',
     'valor': '9'},
    {'naipe': 'C',
     'valor': '10'},
    {'naipe': 'P',
     'valor': '10'},
    {'naipe': 'E',
     'valor': '10'}
]
mao33 = [
    {'naipe': 'O',
     'valor': 'A'},
    {'naipe': 'O',
     'valor': 'A'},
    {'naipe': 'C',
     'valor': 'A'},
    {'naipe': 'P',
     'valor': 'A'},
    {'naipe': 'E',
     'valor': '10'}
]

mao4 = [
    {'naipe': 'O',
     'valor': '9'},
    {'naipe': 'P',
     'valor': '9'},
    {'naipe': 'C',
     'valor': '10'},
    {'naipe': 'P',
     'valor': '10'},
    {'naipe': 'E',
     'valor': '10'}
]

mao5 = [
    {'naipe': 'O',
     'valor': '9'},
    {'naipe': 'O',
     'valor': '2'},
    {'naipe': 'O',
     'valor': '3'},
    {'naipe': 'O',
     'valor': '5'},
    {'naipe': 'O',
     'valor': '10'}
]

mao6 = [
    {'naipe': 'P',
     'valor': '9'},
    {'naipe': 'E',
     'valor': '8'},
    {'naipe': 'O',
     'valor': '10'},
    {'naipe': 'C',
     'valor': 'J'},
    {'naipe': 'E',
     'valor': '7'}
]

mao66 = [
    {'naipe': 'P',
     'valor': 'A'},
    {'naipe': 'E',
     'valor': '2'},
    {'naipe': 'O',
     'valor': '3'},
    {'naipe': 'C',
     'valor': '4'},
    {'naipe': 'E',
     'valor': '5'}
]

mao666 = [
    {'naipe': 'P',
     'valor': 'Q'},
    {'naipe': 'E',
     'valor': 'K'},
    {'naipe': 'O',
     'valor': '10'},
    {'naipe': 'C',
     'valor': 'J'},
    {'naipe': 'E',
     'valor': 'A'}
]

mao7 = [
    {'naipe': 'O',
     'valor': '7'},
    {'naipe': 'O',
     'valor': '9'},
    {'naipe': 'C',
     'valor': '10'},
    {'naipe': 'P',
     'valor': '10'},
    {'naipe': 'E',
     'valor': '10'}
]

mao8 = [
    {'naipe': 'O',
     'valor': '7'},
    {'naipe': 'O',
     'valor': '9'},
    {'naipe': 'C',
     'valor': '7'},
    {'naipe': 'P',
     'valor': '9'},
    {'naipe': 'E',
     'valor': '10'}
]

mao9 = [
    {'naipe': 'O',
     'valor': '7'},
    {'naipe': 'O',
     'valor': '6'},
    {'naipe': 'C',
     'valor': '7'},
    {'naipe': 'P',
     'valor': '9'},
    {'naipe': 'E',
     'valor': '10'}
]

mao10 = [
    {'naipe': 'O',
     'valor': '7'},
    {'naipe': 'O',
     'valor': '6'},
    {'naipe': 'C',
     'valor': '5'},
    {'naipe': 'P',
     'valor': '9'},
    {'naipe': 'E',
     'valor': '10'}
]

fazer_verficacao(mao2)

res1 = fazer_verficacao(mao3)
res2 = fazer_verficacao(mao66)
#
vencedora = compara_maos(res1, res2)
#
# print(vencedora)


