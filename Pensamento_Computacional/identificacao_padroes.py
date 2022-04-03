## Você está no mercado com 20 reais e decidi dividir igualmente o valor que prestende gastar comprando 2 itens

arroz_kg = 7.00
feijao = 9.00
carne_kg = 35.00

for i in range(3):
    valor = input()
    ## função float tenta passar em valor
    valor = float(valor)
    if valor <= 10.00:
        print("Posso comprar!")
    else:
        print("Não posso comprar!")
