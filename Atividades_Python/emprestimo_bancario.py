# Um banco está analisando se um cliente pode receber um emprestimo. Para isso, ele precisa verificar algumas condições antes de aprovar o crédito. O programa deverá: receber a idade, receber o salário, receber o tempo de trabalho, verificar se o cliente pode receber o emprestimo, mostrar o resultado da análise. Regras do sistema : o emprestimo será aprovado se ( idade maior ou igual a 18 anos) (salário maior ou igual a 2000R$) (tempo de trabalho maior ou igual a 2 anos) Regras especiais: Aprovação automática se o salario for maior ou igual a 5000R$ o empréstimo é aprovado automaticamente. Negação automatica quando a idade for menor que 18 anos, o emprestimo é negado automaticamente.

# idade = int(input("Digite a idade do cliente: "))

# if idade < 18:
#     print("Empréstimo negado! Menor de idade não pode solicitar empréstimo.")
#     exit()

# salario = float(input("Digite o salário do cliente: "))
# tempo_trabalho = float(input("Digite o tempo de trabalho do cliente em anos: "))

# if salario >= 5000:
#     print("Empréstimo aprovado! Salário acima de R$ 5000,00.")
# elif tempo_trabalho >= 2 and salario >= 2000:
#     print(f"Empréstimo aprovado! Cliente atendeu aos critérios de idade: {idade} anos, salário: R$ {salario:.2f} e tempo de trabalho: {tempo_trabalho} anos, portanto o emprestimo foi aprovaodo com sucesso!")
# else:
#     print("Empréstimo negado! Cliente não atendeu aos critérios necessários.")


# Agora preciso fazer o valor do emprestimo onde o cliente informa quanto deseja solicitar ao banco, calculo de parcela  = o programa deve calcular o valor de cada parcela com base no emprestimo solicitado, e tem que haver uma verificação se a parcela é maior que 30% do salario. Regra de negocio real: se a parcela comprometer mais que 30% da renda, o crédito é negado. 

valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))
salario = float(input("Digite o salário do cliente: "))
calculo_parcela = valor_emprestimo 
verificacao_parcela = calculo_parcela 

if verificacao_parcela > (salario * 0.3):
    print("Empréstimo negado! A parcela comprometeria mais de 30% da renda do cliente.")
else:
    print(f"emprestimo aprovado! O valor do empréstimo solicitado é de R$ {valor_emprestimo:.2f}, e a parcela comprometerá menos de 30% da renda do cliente.")

