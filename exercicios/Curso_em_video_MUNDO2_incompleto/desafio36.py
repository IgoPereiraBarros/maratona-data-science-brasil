valor_casa = int(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
qtd_anos = int(input('Em quantos anos você pretende pagar (parcelas): '))

prestacao_mensal = valor_casa / (qtd_anos * 12)

if salario * 0.3 <= prestacao_mensal:
    print('Valor a pagar R$ {:.2f} ,00 reais, '.format(prestacao_mensal), end='')
    input('Emprestimo Negado!')
else:
    print('Valor a pagar R$ {:.2f} ,00 reais'.format(prestacao_mensal))
    input('Emprestimo realizado com sucesso!')
