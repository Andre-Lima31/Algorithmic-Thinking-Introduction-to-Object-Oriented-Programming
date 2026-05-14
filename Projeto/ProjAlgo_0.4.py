Valor_APagar = float(0)
Compra_Fechada = False

#Fazer um cadastro/login, aonde pergunta se a pessoa tem crianças aqui, para ficar mais discreto o desconto.

while Compra_Fechada == False:
    print("Bem vindo(a)! Empresa R.M vós das boas vindas ao nosso programa de criação de orçamento. Informe-nos sobre o imóvel que deseja usando as opções a baixo.")
    print("a qualquer momento, digite <'Ret'> para retornar a questão anterior.")
    print('\t')
    Tipo = str(input('''###------------------------------------###
1) quero um Apartamento {R$ 700,00 - 1 quarto}
2) quero uma Casa {R$ 900,00 - 1 quarto}
3) quero um Estudio {R$ 1200,00}
> '''))
    print("###------------------------------------###")
    print("\t")
    if Tipo == '1':
        Quartos_Resposta = False
        Estacionamento_Resposta = 'n'
        Valor_APagar = (Valor_APagar + 700)
        print ("Você selecionou: Apartamento")
        Quartos = str(input('''Quantos quartos você deseja? Opções disponiveis:
1) Apenas 1 quarto.
2) Desejo 2 quartos.
> '''))
        while Quartos_Resposta == False:
            if Quartos[0] == 'r':
                Valor_APagar = 0
                break
            elif Quartos == '1':
                Quartos = int(1)
                Quartos_Resposta = True
                Estacionamento_Resposta = False
                break
            elif Quartos == '2':
                Quartos = int(2)
                Valor_APagar = (Valor_APagar + 200)
                Quartos_Resposta = True
                Estacionamento_Resposta = False
                break
            else:
                print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                break
        while Estacionamento_Resposta == False:
            break
    elif Tipo == '2':
        Valor_APagar = (Valor_APagar + 900)
    elif Tipo == '3':
        Valor_APagar = (Valor_APagar + 1200)
    elif Tipo[0] == 'r' and Tipo[1] == 'e' and Tipo[2] == 't':
        print ("[x] - Não há outra questão anterior a esta.")
    else:
        print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
