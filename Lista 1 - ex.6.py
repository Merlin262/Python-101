gastoIngredientes = float(input("Informe o gasto em ingredientes "))
producao = float(input("Informe a quantidade produzida com os ingredientes "))

valorKilo = float(gastoIngredientes/producao)

print("O valor por quilos sera de R$" + str(valorKilo)+"/kg")