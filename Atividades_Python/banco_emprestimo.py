
# Um banco está analisando se um cliente pode receber um emprestimo. Para isso, ele precisa verificar algumas condições antes de aprovar o crédito. O programa deverá: receber a idade, receber o salário, receber o tempo de trabalho, verificar se o cliente pode receber o emprestimo, mostrar o resultado da análise. Regras do sistema : o emprestimo será aprovado se ( idade maior ou igual a 18 anos) (salário maior ou igual a 2000R$) (tempo de trabalho maior ou igual a 2 anos) Regras especiais: Aprovação automática se o salario for maior ou igual a 5000R$ o empréstimo é aprovado automaticamente. Negação automatica quando a idade for menor que 18 anos, o emprestimo é negado automaticamente.

idade = int(input("Digite a idade do cliente: "))

if idade < 18:
    print("Empréstimo negado! Menor de idade não pode solicitar empréstimo.")
    exit()

salario = float(input("Digite o salário do cliente: "))
tempo_trabalho = float(input("Digite o tempo de trabalho do cliente em anos: "))

if salario < 2000 or tempo_trabalho < 2:
    print("Empréstimo negado! Cliente não atendeu aos critérios necessários.")
    exit()

valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))
calculo_parcela = valor_emprestimo

if calculo_parcela > (salario * 0.3):
    print("Empréstimo negado! A parcela comprometeria mais de 30% da renda do cliente.")
elif salario >= 5000:
    print(f"Empréstimo aprovado automaticamente! Cliente com {idade} anos e salário de R$ {salario:.2f}.")
else:
    print(f"Empréstimo aprovado! Cliente com {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} anos de trabalho.")
    print(f"Valor solicitado: R$ {valor_emprestimo:.2f}. A parcela comprometerá menos de 30% da renda.")
