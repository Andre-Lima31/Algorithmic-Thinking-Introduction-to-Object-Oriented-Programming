import csv

with open("parcelas_RM.csv", 'w', newline="", encoding = 'utf-8') as RM:
    editar = csv.writer(RM)
    editar.writerows()

