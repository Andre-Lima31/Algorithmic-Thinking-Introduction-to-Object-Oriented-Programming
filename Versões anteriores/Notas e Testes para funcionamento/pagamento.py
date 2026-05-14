valor_total = float(input("Digite o valor da compra: R$"))
valor_pagar = 0
print ('\t')

opcao_escolha = str(input('''Escolha a maneira de pagamento:
(A) - Dinheiro
(B) - Boleto
(C) - Credito
(D) - Debito
(E) - PIX
>'''))

parcela_disp = False

if opcao_escolha.lower() == 'a':
    escolha = 'Dinheiro'
elif opcao_escolha.lower() == 'b':
    escolha = "Boleto"
    parcela_disp = True
elif opcao_escolha.lower() == 'c':
    escolha = "Credito"
elif opcao_escolha.lower() == 'd':
    escolha = "Debito"
elif opcao_escolha.lower() == 'e':
    escolha = "PIX"
else:
    print ("Opção não e valida.")

if opcao_escolha.lower() == 'c' or opcao_escolha.lower() == 'd':
    valor_pagar = round(valor_total *(1 - 0.10), 2)
elif opcao_escolha.lower() == 'e':
    valor_pagar = round(valor_total*(1 - 0.15), 2)
elif parcela_disp == True:
    parcela = str(input('''Deseja parcelar sua compra?
    S = Sim | N = Não.
    > '''))
    if parcela.lower() == 's':
        parcela_valor = int(input("Em quantas vezes pretende parcelar? Você pode parcelar em até 8 vezes: "))
        if parcela_valor > 1 and parcela_valor < 9:
            valor_pagar = round(valor_total/parcela_valor, 2)
            print('Você pagará o valor de R$'+str(valor_total)+' em', parcela_valor, 'parcelas de R$'+str(valor_pagar))
        else:
            print('Valor indisponivel. Parcelamento Cancelado')
            valor_pagar = round(valor_total, 2)
    else:
        print ("parcelamento não aceito.")
        valor_pagar = round(valor_total, 2)
else:
    valor_pagar = valor_total

print('R$'+str(valor_pagar),'em', escolha)
