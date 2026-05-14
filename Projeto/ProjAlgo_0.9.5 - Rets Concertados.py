Valor_APagar = float(0)
Valor_Calculado = False
Compra_Fechada = False
Quartos_Resposta = False
Estacionamento_Resposta = False

#Fazer um cadastro/login, aonde pergunta se a pessoa tem crianças aqui, para ficar mais discreto o desconto.
Child = False

while Compra_Fechada == False:
    while Valor_Calculado == False:
        print("Bem vindo(a)! Empresa R.M vós das boas vindas ao nosso programa de criação de orçamento. Informe-nos sobre o imóvel que deseja usando as opções a baixo.")
        print("a qualquer momento, digite <'return'> para retornar a questão anterior.")
        Tipo = str(input('''###------------------------------------###
1) quero um Apartamento {R$ 700,00 - 1 quarto}
2) quero uma Casa {R$ 900,00 - 1 quarto}
3) quero um Estudio {R$ 1200,00}
> '''))
        print("\t")
        if Tipo == '1':
            Imovel = "Apartamento"
            Valor_APagar = (Valor_APagar + 700)
            print ("Você selecionou: Apartamento")
            Quartos = str(input('''Quantos quartos você deseja? Opções disponiveis:
1) Apenas 1 quarto.
2) Desejo 2 quartos.
> '''))
            while Quartos_Resposta == False:
                if Quartos[0].lower() == 'r':
                    print("###------------------------------------###")
                    print ('\n')
                    Valor_APagar = 0
                    break
                elif Quartos == '1':
                    Quartos = int(1)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                elif Quartos == '2':
                    Quartos = int(2)
                    Valor_APagar = (Valor_APagar + 200)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    break
            while Estacionamento_Resposta == True:
                print ('\t')
                print ("Você deseja um apartamento com", Quartos, "quartos. Você deseja alugar uma vaga de garagem?")
                print ("1) Sim.")
                print ("2) Não.")
                Garagem = str(input ("> "))
                if Garagem.lower() == 'r':
                    if Quartos == 2:
                        Valor_APagar = (Valor_APagar - 200)
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                    else:
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                elif Garagem == '1':
                    Valor_Calculado = True
                    Valor_APagar = (Valor_APagar + 300)
                    break
                elif Garagem == '2':
                    Valor_Calculado = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    break
            if Child == False:
                    Valor_APagar = Valor_APagar * (1 - 0.05)
            else:
                    pass
            break
        elif Tipo == '2':
            Valor_APagar = (Valor_APagar + 900)
            Imovel = "casa"
            print ("Você selecionou: Casa")
            Quartos = str(input('''Quantos quartos você deseja? Opções disponiveis:
1) Apenas 1 quarto.
2) Desejo 2 quartos.
> '''))
            while Quartos_Resposta == False:
                if Quartos[0].lower() == 'r':
                    print("###------------------------------------###")
                    print ('\n')
                    Valor_APagar = 0
                    break
                elif Quartos == '1':
                    Quartos = int(1)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                elif Quartos == '2':
                    Quartos = int(2)
                    Valor_APagar = (Valor_APagar + 250)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    break
            while Estacionamento_Resposta == True:
                print ('\t')
                print ("Você deseja uma casa com", Quartos, "quartos. Você deseja alugar uma vaga de garagem?")
                print ("1) Sim.")
                print ("2) Não.")
                Garagem = str(input ("> "))
                if Garagem.lower() == 'r':
                    if Quartos == 2:
                        Valor_APagar = (Valor_APagar - 250)
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                    else:
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                elif Garagem == '1':
                    Valor_Calculado = True
                    Valor_APagar = (Valor_APagar + 300)
                    break
                elif Garagem == '2':
                    Valor_Calculado = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    break
            if Child == False:
                    Valor_APagar = Valor_APagar * (1 - 0.05)
            else:
                    pass
            break
        elif Tipo == '3':
            Valor_APagar = (Valor_APagar + 1200)
        elif Tipo[0] == 'r' and Tipo[1] == 'e' and Tipo[2] == 't':
            print ("[x] - Não há outra questão anterior a esta.")
        else:
            print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
    if Valor_Calculado == True:
        print ('\t')
        print ('Calculando.')
        print ("Calculando..")
        print ('Calculando...')
        print ("Pronto!")
        print ('\n')
        print ('###------------------------------------###')
        while Valor_Calculado == True:
                print ("O imovel, "+str(Imovel)+", desejado custará R$"+str(Valor_APagar)+" por mês, podendo ser parcelado em até 5 vezes.")
                print ("1) Desejo pagar a vista.")
                print ("2) Desejo parcelar.")
                print ("[*] - Digite <'return'> para voltar cancelar a operação e voltar ao menu inicial.")
                Parcela = str(input("> "))
                if Parcela[0].lower() == 'r':
                    print ('\n')
                    print ('###------------------------------------###')
                    Valor_Calculado = False
                    break
                elif Parcela == '1':
                    print ('Você escolheu pagar', Valor_APagar, "a vista.")
                    confirm = str(input("deseja gerar um documento .cvs contendo as informações? Digite 'confirmo' para seguir com o pagamento: >"))
                    if confirm.lower() == 'confirmo':
                        #gerar .cvs
                        print('Operação Concluida com Sucesso! Obrigado pela preferencia.')
                        Valor_Calculado = True
                        Compra_Fechada = True
                        break
                    else:
                        print('Operação Cancelada. Obrigado pela preferencia.')
                        break
                elif Parcela == '2':
                    while True:
                        Qnt_Parcela = int(input("Insira a quantidade de vezes a ser parcelada: "))
                        if Qnt_Parcela == 1:
                            print ("Parcelando 1 vez, o(a) senhor(a) desejou o mesmo de pagar a vista. R$"+str(Valor_APagar))
                            Valor_Calculado = True
                            Compra_Fechada = True
                            break
                        elif Qnt_Parcela > 1 and Qnt_Parcela < 6:
                            Valor_APagar = round(Valor_APagar/Qnt_Parcela, 2)
                            print ("Parcelando", Qnt_Parcela, "vezes, você pagara R$"+str(Valor_APagar)+" por mês")
                            Valor_Calculado = True
                            Compra_Fechada = True
                            break
                        else:
                            print('[x] - Atenção, a quantia de parcelas deve ser até 5 vezes.')
                    confirm = str(input("deseja gerar um documento .cvs contendo as informações? Digite 'confirmo' para seguir com o pagamento: >"))
                    if confirm.lower() == 'confirmo':
                        #gerar .cvs
                        print('Operação Concluida com Sucesso! Obrigado pela preferencia.')
                        Valor_Calculado = True
                        Compra_Fechada = True
                        break
                    else:
                        print('Operação Encerrada. Obrigado pela preferencia.')
                        break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
    else:
        pass
