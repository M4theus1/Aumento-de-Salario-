salario = float(input('Informe o seu salário para calcularmos o seu aumento: R$'))
if salario > 1250:
    aumento = salario + (salario * (10/100))
if salario < 1250:
    aumento = salario + (salario * (15/100))
print(' ')
print('Pronto! O seu salário com os reajustes ficou de: R${:.2f}'.format(aumento))