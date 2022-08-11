preco=float(input("Informe o preco do produto"))

valor5Juros=preco*1.05
valor5JurosParcelados=valor5Juros/3

valorParcela2Vezes=preco/2

valor5Desc=preco/1.05

print(f"O valor em 3 vezes eh de " + str(valor5JurosParcelados) + ","+ "\n"+ "o valor em 2 vezes eh de " + str(valorParcela2Vezes))  
print(f"e o valor a vista eh de {valor5Desc:.2f}")
