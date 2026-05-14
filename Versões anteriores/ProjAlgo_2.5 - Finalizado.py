import csv
import datetime

Usuario_Registrado = False
Valor_Calculado = False
Compra_Fechada = False

while Usuario_Registrado == False:
    print ("Bem vindo(a) ao catalogo de imoveis da R.M., aqui você pode conferir tipos de imoveis diposniveis para alguel e venda, assim como seus preços. Vamos começar?")
    nome = str(input(">Insira seu nome por favor: "))
    if nome.isnumeric() == False and len(nome) > 0 and not " " in nome:
        while True:
          try: 
            idade = int(input(">Digite sua idade: "))
            if int(idade) >= 18:
                filhos = str(input(">Caso possua filhos, quantos? Caso não digite '0': "))
                if int(filhos) == 0:
                    usuario = [nome, idade, False]
                    Usuario_Registrado = True                    
                    break
                elif int(filhos) < 0:
                    print ('\t')
                    print ('[x] - Erro. Por favor insira um valor valido.')
                    print ('\t')
                else:
                    usuario = [nome, idade, True]
                    Usuario_Registrado = True
                    break
            else:
                print ('\t')
                print("[x] - Erro. Apenas usuario com maior de 18 podem seguir.")
                print ('\t')
                break
          except ValueError:
               print ("[x] - Erro. Por favor, digite um numero.")
               print ('\t')
    else:
        print ('\t')
        print ("[x] - Erro. Por favor, digite seu nome, e somente seu primeiro nome.")
        print ('\t')

print ("\n")

while Compra_Fechada == False:
    while Valor_Calculado == False:
        print("Bem vindo(a) "+str(usuario[0])+"! A Empresa R.M vós das boas vindas ao nosso programa de planejamento de orçamento. Informe-nos sobre o imóvel que deseja usando as opções a baixo e calcularemos o aluguel mensal e o contrato imobiliario.")
        print("a qualquer momento, digite <'ret'> para retornar ao menu inicial, esta pagina.")
        Valor_Aluguel = float(0)
        Quartos_Resposta = False
        Estacionamento_Resposta = False
        Tipo = str(input('''###------------------------------------###
1) quero um Apartamento {R$ 700,00 - 1 quarto}
2) quero uma Casa {R$ 900,00 - 1 quarto}
3) quero um Estudio {R$ 1200,00}
> '''))
        print("\t")
        if Tipo == '1':
            Imovel = "Apartamento"
            Valor_Aluguel = (Valor_Aluguel + 700)
            print ("Você selecionou: Apartamento")
            Quartos = str(input('''Quantos quartos você deseja? Opções disponiveis:
1) Apenas 1 quarto.
2) Desejo 2 quartos.
> '''))
            while Quartos_Resposta == False:
                if Quartos[0].lower() == 'r':
                    print("###------------------------------------###")
                    print ('\n')
                    Valor_Aluguel = 0
                    break
                elif Quartos == '1':
                    Quartos = int(1)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                elif Quartos == '2':
                    Quartos = int(2)
                    Valor_Aluguel = (Valor_Aluguel + 200)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
                    break
            while Estacionamento_Resposta == True:
                print ('\t')
                print ("Você deseja um apartamento com", Quartos, "quartos. Você deseja alugar uma vaga de garagem?")
                print ("1) Sim.")
                print ("2) Não.")
                Garagem = str(input ("> "))
                if Garagem[0].lower() == 'r':
                    if Quartos == 2:
                        print("###------------------------------------###")
                        print ('\n')
                        Valor_Aluguel = (Valor_Aluguel - 200)
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                    else:
                        Quartos_Resposta = False
                        Estacionamento_Resposta = False
                        break
                elif Garagem == '1':
                    Valor_Calculado = True
                    Valor_Aluguel = (Valor_Aluguel + 300)
                    break
                elif Garagem == '2':
                    Valor_Calculado = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
                    break
            if usuario[2] == False:
                    Valor_Aluguel = Valor_Aluguel * (1 - 0.05)
            else:
                    pass
            break
        elif Tipo == '2':
            Valor_Aluguel = (Valor_Aluguel + 900)
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
                    Valor_Aluguel = 0
                    break
                elif Quartos == '1':
                    Quartos = int(1)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                elif Quartos == '2':
                    Quartos = int(2)
                    Valor_Aluguel = (Valor_Aluguel + 250)
                    Quartos_Resposta = True
                    Estacionamento_Resposta = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
                    break
            while Estacionamento_Resposta == True:
                print ('\t')
                print ("Você deseja uma casa com", Quartos, "quartos. Você deseja alugar uma vaga de garagem?")
                print ("1) Sim.")
                print ("2) Não.")
                Garagem = str(input ("> "))
                if Garagem[0].lower() == 'r':
                    print("###------------------------------------###")
                    print ('\n')
                    Quartos_Resposta = False
                    Estacionamento_Resposta = False
                    break
                elif Garagem == '1':
                    Valor_Calculado = True
                    Valor_Aluguel = (Valor_Aluguel + 300)
                    break
                elif Garagem == '2':
                    Valor_Calculado = True
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
                    break
            break
        elif Tipo == '3':
            Valor_Aluguel = (Valor_Aluguel + 1200)
            Imovel = "Estudio"
            print ("Você selecionou: Estudio")
            print ("\n")
            Vaga_Resposta = False
            print ("Você deseja obter uma vaga de estacionamento extra?")
            Vagas = str(input('''Com 2 vagas por R$250,00 e mais de duas por R$60,00 cada.
1) Não.
2) Quero uma, ou mais, vagas extras.
> '''))
            while Vaga_Resposta == False:
                if Vagas[0].lower() == 'r':
                    print("###------------------------------------###")
                    print ('\n')
                    Valor_Aluguel = 0
                    break
                elif Vagas == '2':
                    Vaga_Resposta = True
                    print ('\t')
                elif Vagas == '1':
                    Valor_Calculado = True
                    print ('\t')
                    break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
                    break
            if Vaga_Resposta == True:
                loop = True
                while loop == True:
                    Vagas_Extra = str(input('''Insira a quantia de vagas extras desejadas.
>'''))
                    if Vagas_Extra[0].lower() == 'r':
                        print("###------------------------------------###")
                        print ('\n')
                        Valor_Aluguel = 0
                        Vaga_Resposta = False
                        break
                    elif Vagas_Extra.isnumeric() == True and int(Vagas_Extra) >= 0:
                        Valor_Aluguel = Valor_Aluguel + 250 + ((int(Vagas_Extra)-1)*60)
                        Vagas_Total = int(Vagas_Extra) + 1
                        print ('')
                        print("Você deseja obter um estudio com", Vagas_Total, "vagas no total? 'Sim' ou 'Não'")
                        print ("[*] - Você pode digitar <ret> a qualquer momento para retornar a questão anterior")
                        confirm = str(input("> "))
                        while True:
                            if confirm[0].lower() == 'r':
                                loop = False
                                Vaga_Resposta = False
                                print('\n')
                                break
                            elif confirm.lower() == 'sim':
                                Valor_Calculado = True
                                loop = False
                                break
                            elif confirm[0].lower() == 'n':
                                print ('')
                                break
                            else:
                                print('[x] - Opção Invalida. Por favor, digite <Sim> ou <Não>')
                                print ('\t')
                    else:
                       print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                       print ('\t')
            else:
                pass
        elif Tipo[0] == 'r' and Tipo[1] == 'e' and Tipo[2] == 't':
            print ("[x] - Você já esta no menu inicial.")
            print ('\t')
        else:
            print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
            print ('\t')
    if Valor_Calculado == True:
        print ('\t')
        print ('Calculando.')
        print ("Calculando..")
        print ('Calculando...')
        print ("Pronto!")
        print ('\n')
        print ('###------------------------------------###')
        while Valor_Calculado == True:
                print ("O imovel, "+str(Imovel)+", desejado custará um aluguel mensal de R$"+str(int(Valor_Aluguel))+",00")
                print ("O contrato imobiliario é de R$2000,00 e pode ser parcelado em até 5 vezes")
                print ("1) Desejo pagar à vista.")
                print ("2) Desejo parcelar.")
                print ("3) não estou satisfeito com esse valor, quero cancelar e voltar ao menu de opções inicial.")
                Parcela_Confirm = str(input("> "))
                if Parcela_Confirm == '3' or Parcela_Confirm[0].lower() == 'r':
                    print ('\n')
                    print ('###------------------------------------###')
                    Valor_Calculado = False
                    break
                elif Parcela_Confirm == '1':
                    print ('Você escolheu pagar R$2000,00 à vista.')
                    confirm = str(input("Digite 'confirmo' para seguir com o pagamento: >"))
                    if confirm.lower() == 'confirmo':
                        print('Operação Concluida com Sucesso! Obrigado pela preferencia.')
                        Qnt_Parcela = int(1)
                        Valor_Calculado = True
                        Compra_Fechada = True
                        break
                    else:
                        print('Operação Cancelada. Obrigado pela preferencia.')
                        break
                elif Parcela_Confirm == '2':
                    while True:
                        Qnt_Parcela = int(input("Insira a quantidade de vezes a ser parcelada: "))
                        if Qnt_Parcela == 1:
                            print ('\t')
                            print ("Parcelando 1 vez, o(a) senhor(a) desejou o mesmo de pagar à vista. R$2000,00")
                            Valor_Calculado = True
                            Compra_Fechada = True
                            break
                        elif Qnt_Parcela > 1 and Qnt_Parcela < 6:
                            contrato = round((2000/int(Qnt_Parcela)), 2)
                            print ('\t')
                            print ("Parcelando", Qnt_Parcela, "vezes, você pagara R$"+str(contrato)+" por mês acima do seu aluguel de R$"+str(int(Valor_Aluguel))+",00 pelos primeiros", Qnt_Parcela, "meses.")
                            Valor_Final = round(float(Valor_Aluguel) + float(contrato), 2)
                            print ("Para um total de R$"+str(Valor_Final)+" durante esse periodo, antes de retornar ao aluguel base de R$"+str(int(Valor_Aluguel))+",00")
                            Valor_Calculado = True
                            Compra_Fechada = True
                            break
                        else:
                            print('[x] - Atenção, a quantia de parcelas deve ser até 5 vezes.')
                            print ('\t')
                    confirm = str(input("Se este valor esta aceitavel, digite 'confirmo' para seguir com o pagamento: >"))
                    if confirm.lower() == 'confirmo':
                        print('Operação Concluida com Sucesso!')
                        Valor_Calculado = True
                        Compra_Fechada = True
                        break
                    else:
                        print('Operação Cancelada. Obrigado pela preferencia.')
                        print ('\t')
                        break
                else:
                    print ("[x] - Opção Invalida. Por favor, insira uma opção valida.")
                    print ('\t')
    else:
        pass

while Valor_Calculado == True and Compra_Fechada == True:
    print ('\t')
    csv_confirma = str(input('''Antes de sair. Gostaria de gerar uma planilha contendo informações sobre as parcelas?
1)Sim
2)Não
>'''))
    if csv_confirma == '2':
        print ('\t')
        print ("Entendido. R.M. agradeçe a preferencia.")
        break
    elif csv_confirma == '1':
        data = (datetime.date.today() + datetime.timedelta(days=30))
        with open("parcelas_RM.csv", 'w', newline="", encoding = 'utf-8-sig') as RM:
            editar = csv.writer(RM, delimiter = ";")
            editar.writerow(["Nº da Parcela;", "Cliente;", "Aluguel", "Contrato Imobiliario", "Total A Pagar (R$)", "Referente a;", "Data de Vencimento;", "Pago;"])
        for i in range (0, 12):
            i = i+1
            if i <= Qnt_Parcela:
                pass
            else:
                Valor_Final = Valor_Aluguel
                contrato = 0
            parcelas = []
            parcelas.append(str(i)+";")
            parcelas.append(str(usuario[0])+";")
            parcelas.append("R$"+str(Valor_Aluguel)+";")
            parcelas.append("R$"+str(contrato)+";")
            parcelas.append("R$"+str(Valor_Final)+";")
            parcelas.append("Empresa R.M.;")
            parcelas.append(str(data.strftime("%d/%m/%Y"))+";")
            parcelas.append("( );")
            with open("parcelas_RM.csv", 'a', newline="", encoding = 'utf-8-sig') as RM:
                editar = csv.writer(RM, delimiter = ";")
                editar.writerow(parcelas)
            data = (data + datetime.timedelta(days=31))
        print ("Operação Concluida com Sucesso! Obrigado pela preferencia.")
        break
    else:
        print('[x] - Erro. Por favor insira um digito valido.')
        print ('\t')
