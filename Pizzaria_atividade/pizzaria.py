# A Pizzaria do sabores cobra o frente de acordo com a distancia entre a pizzaria e a casa do cliente. Sua tarefa é descobrir quanto custa a entrega para cada cliente.


# distancia = float(input("digite a distância em km: "))
# if distancia <= 5:
#     print("O frete será de 5 reais")
# elif distancia <= 10:
#     print("O frete será de 10 reais")
# else:
#     print("Não entregamos nesse raio de distancia")

# Agora a pizzaria cobra uma taxa fixa de R$ 5,00 por entrega, somada a um valor por quilômetro que depende da faixa de distancia 

# distancia = float(input("Digite a distância em km: "))
# taxa_fixa = 5.0  # Taxa fixa para entregas até 5 km
# if distancia <= 5:
#     valor_km = 1.0
#     print ("O valor por Km é de : R$ {:.2f}".format(valor_km))
# elif distancia <= 10:
#     valor_km = 2.0
#     print ("O valor por Km é de : R$ {:.2f}".format(valor_km))
# else:
#     print("Não entregamos nesse raio de distância")
#     exit()  
    # Encerra o programa se a distância for maior que 10 km

# Para atrair clientes, a pizzaria criou promoções que dependem do dia da semana. Sobre o valor do pedido soma-se uma taxa de entrega de R$ 5,00, exceto quando a promoção der frete gratis 

# dia = input("Dia da semana: ").lower()
# valor = float(input("Valor do pedido: R$ "))
# desconto = valor * 0.15

# if dia == "terça-feira" and valor > 40:
#     total = valor + 5.0
#     print("A sobremesa sairá de graça. O valor total, com R$ 5,00 de frete, é de R$ {:.2f}".format(total))
# elif dia == "quarta-feira":
#     desconto = valor * 0.15
#     total = valor - desconto + 5.0
#     print("Você ganhou 15% de desconto na pizza. O valor final, com frete, é de R$ {:.2f}".format(total))

# elif (dia == "sábado" or dia == "domingo") and valor > 100:
#     valor_final = valor
#     print("Frete grátis nesses dias, o valor do pedido é de R$ {:.2f}".format(valor_final))
# else: 
#     valor_final = valor + 5.0
#     print("Os demais dias da semana não possuem promoções. O valor total, com R$ 5,00 de frete, é de R$ {:.2f}".format(valor_final))
