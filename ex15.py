print("Vamos calcular o valor do seu salario por hora!")
salario = float(input("Informe o seu salario: "))
dias = int(input(" Informe quantos dias trabalha no mês: "))
horas = int(input("Informe quantas horas trabalhadas por dia: "))
resul = (salario/dias)/horas
print("O seu salario mensal é R$",salario," e o valor por horas está no total de: R$",resul)