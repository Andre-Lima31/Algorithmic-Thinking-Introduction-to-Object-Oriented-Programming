Valor_APagar = float(0)

while True:
    print("Bem vindo(a)! Empresa R.M vós das boas vindas ao nosso programa de criação de orçamento. Informe-nos sobre o imóvel que deseja usando as opções a baixo.")
    print("a qualquer momento, digite <'Ret'> para retornar a questão anterior, e <'Cancel'> para encerrar sua sessão.")
    print('\t')
    Tipo = str(input('''###------------------------------------###
A) quero um Apartamento
B) quero uma Casa 
C) quero um Estudio
> ''')).lower()
    if Tipo == 'a':
        #apartamento
    elif Tipo == 'b':
        #casa
    elif Tipo == 'c':
        #estudio
    elif Tipo[0] == 'r' and Tipo[1] == 'e' and Tipo[2] == 't':
        print ("[x] - Não há outra questão anterior a esta.")
    elif Tipo [0] == 'c':
        break
    else:
        print ("[x] - Opção Invalida, por favor, insira uma opção valida.")
