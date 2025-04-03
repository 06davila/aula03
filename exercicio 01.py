nome = input ("digite seu nome: ")
idade = int(input("digite sua idade: "))
salario = float(input("digite seu salario: "))
percentual =float(input("digite seu percentual: "))

porcentagem = (salario*percentual)
salarioatual = (percentual+salario)

print(f"olá {nome}, sua idade é {idade} anos, voce recebe {salario:.2f}, teve aumento de R${porcentagem:.2f} e seu salario atual é R${salarioatual:.2f}. ")





