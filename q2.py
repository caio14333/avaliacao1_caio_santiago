#questao 2
num_produtos = int(input("Quantos produtos foram vendidos? "))
total_vendas = 0
contagem_maior_50 = 0
contagem_menor_50 = 0
for i in range(num_produtos):
    while True: 
            valor_produto = float(input(f"Digite o valor do produto {i+1}: R$ "))
            break 
    total_vendas += valor_produto
    if valor_produto > 50:
        contagem_maior_50 += 1
    else:
        contagem_menor_50 += 1
print(" Resumo das Vendas")
print(f"Valor total dos produtos vendidos: R$ {total_vendas:.2f}")
print(f"Quantidade de produtos com valor > 50 reais: {contagem_maior_50}")
print(f"Quantidade de produtos com valor < 50 reais: {contagem_menor_50}")