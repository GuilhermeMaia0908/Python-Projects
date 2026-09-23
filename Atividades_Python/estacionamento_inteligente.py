# na chegada do estacionamento o motorista informa (idade, se possui cadastro no shopping, o tipo de veiculo, e se o cliente é vip)o sistema ira permitir ou não a entrada do veiculo. O programa deve receber informações do motorista e , com base nas regras do estacionamento, decidir se o veiculo pode ou não pode entrar. Situações obs : motoristas jovens não podem entrar sozinhos, veiculo maior tem regras diferentes, liberação rapida algs clientes foram liberados sem precisar de verificação e entrada negada em certos casos, o mesmo com cadastro, a entrada sera negada. Perguntas a se pensar ( existe alguma situação que impede a entrada imediatamente? ) (Quais condições precisam ser atendidas ao mesmo tempo?) ( existe alguma situação que libera a entrada automaticamente?) ( qual deve ser a ordem das verificações?)

idade = int(input("Digite a idade do motorista: "))
cadastro = input("O motorista possui cadastro no shopping? (sim/não): ")
tipo_veiculo = input("Digite o tipo de veículo (carro/moto/caminhão): ")
vip = input("O cliente é VIP? (sim/não): ")

if cadastro.lower() == "sim" or vip.lower() == "sim":
    print("Entrada Liberada automaticamente: cliente cadastrado ou VIP.")
elif idade < 18:
    print("Entrada Negada: Motoristas menores de idade não podem entrar sozinhos.")
elif tipo_veiculo.lower() == "caminhão" and cadastro.lower() != "sim":
    print("Entrada Negada: Veículos maiores têm regras diferentes e não é permitido entrar sem cadastro.")
else:
    print("Entrada Permitida: O veículo pode entrar no estacionamento.")