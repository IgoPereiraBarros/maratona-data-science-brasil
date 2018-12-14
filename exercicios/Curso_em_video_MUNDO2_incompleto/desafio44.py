preco_normal = float(input('Informe o preço do produto: '))
condicao_pagamento = str(input('Informe a forma de pagamento do produto (Dinheiro, Cheque ou Cartão): ')).upper().lower()


if condicao_pagamento == 'cheque' or condicao_pagamento == 'dinheiro':
    total = preco_normal - (preco_normal * 0.1)
    print('Total a pagar R$ {} ,00 reais'.format(total))
elif condicao_pagamento == 'cartao':
    fp = int(input('Quantas vezes no cartão, 2x ou 3x ? '))
    total = preco_normal - (preco_normal * 0.05)
    print('Total a pagar R$ {} , 00 reais'.format(total))
    if fp == 2:
        print('Total a pagar R$ {} , 00 reais'.format(preco_normal))
    elif fp == 3:
        total = preco_normal + (preco_normal * 0.2)
        print('Total a pagar R$ {} , 00 reais'.format(total))



