# Objetivo, Criar uma calculadora simples em pyhon, que receba dois numeros e uma operação matematica, e no final ela exibe o resultado da operação. As operações matematicas realizadas são: soma +, subtração -, multiplicação *, divisão /, potenciação **, resto da divisão %.

calculadora = input("Digite a Operação (+,-,*,/,**,%) que deseja fazer:")
num1 = float(input ("Digite o primeiro número: "))
num2 = float(input ("Digite o segundo número: "))

if calculadora == "+":
    resultado = num1 + num2
    print ("O resultado da soma será: {:.2f}" .format(resultado))
elif calculadora == "-":
    resultado = num1 - num2 
    print ("O resultado da subtração será: {:.2f}" .format(resultado))
elif calculadora == "*":
    resultado = num1 * num2 
    print(f"O resultado da multiplicação é: {resultado:.2f}")
elif calculadora == "/":
    if num2 == 0:
        print("Erro: Divisão por zero!")
    else:
        resultado = num1 / num2
        print ("O resultado da divisão será: {:.2f}" .format(resultado))
elif calculadora == "**":
    resultado = num1 ** num2 
    print ("O resultado da potenciação será: {:.2f}" .format(resultado))
elif calculadora == "%":
    resultado = num1 % num2 
    print ("O resultado do resto da divisão será: {:.2f}" .format(resultado))
else:
    print("Operação invalida! Use +, -, *, /, ** ou %.")
# no final é para definir que a operação foi errada na hora do erro de digito 
