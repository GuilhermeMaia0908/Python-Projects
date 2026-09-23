#Criar um programa onde (receba a idade do aluno)(receba a nota da prova)(receba a frequencia escolar em (em %)) (Analise se a matricula pode ser aprovada)(exiba o resultado na tela ) Regra:a matricula sera aprovada se a idade for maior que 18 anos, a nota for maior que 6.0 e a frequencia escolar for maior que 75% (exiba o resultado na tela) -> se a nota for maior ou igual a 9 -> a matricula sera aprovada automaticamente se a idade for menor que 18 anos -> a matricula será negada automaticamente 

idade = int(input("Digite a idade do aluno: "))
nota = float(input("Digite a nota da prova: "))
frequencia = float(input("Digite a frequencia escolar em %: "))

if idade < 18:
    print("A matricula será negada, Aluno menor de idade!")
elif nota >= 9:
    print("A matricula será aprovada automaticamente!")
elif idade >= 18 and nota > 6.0 and frequencia > 75:
    print("A matricula está aprovada!")
else:
    print("A matricula não está aprovada!")

