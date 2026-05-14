Valor_APagar = float(0)
Compra_Fechada = False

while True:
    print("Bem vindo(a)! Empresa R.M vós das boas vindas ao nosso programa de criação de orçamento. Informe-nos sobre o imóvel que deseja usando as opções a baixo.")
    print("a qualquer momento, digite <'Ret'> para retornar a questão anterior, e <'Cancel'> para encerrar sua sessão.")
    print('\t')
    Tipo = str(input("###------------------------------------###\nA) quero um Apartamento {R$ 700,00 - 1 quarto}\tB) quero uma Casa {R$ 900,00 - 1 quarto}\tC) quero um Estudio {R$ 1200,00}\t> ")).lower()
    if Tipo == 'a':
        Valor_APagar = (Valor_APagar + 700)
        print ("Você selecionou: Apartamento")
        print ("")
        while Compra_Fechada == False:
            break
    elif Tipo == 'b':
        Valor_APagar = (Valor_APagar + 900)
    elif Tipo == 'c':
        Valor_APagar = (Valor_APagar + 1200)
    elif Tipo[0] == 'r' and Tipo[1] == 'e' and Tipo[2] == 't':
        print ("[x] - Não há outra questão anterior a esta.")
    elif Tipo [0] == 'c':
        break
    else:
        print ("[x] - Opção Invalida, por favor, insira uma opção valida.")
