from cmath import pi
from sys import float_info


raio=int(input("Informe o raio"))
altura=int(input("Informe a altura"))

#cada 50 reais equivale a 15m^2

circunferencia=2*pi*raio
areaLateral=circunferencia*altura
areaCircular=pi*(raio**2)
qtDeLatas=(areaCircular+areaLateral/15)
valorFinal=qtDeLatas*50

print(f"O custo total equivale a  {valorFinal:.2f}" + f" reais e a quantidade de latass e {qtDeLatas:.2f}")

#PS: Seria possivel fazer um "if qtDeLatas==float:
#                                   qtDeLatas=qtDeLatas+1 ?
# Para não ficar um numero "quebrado" quando deveria ser inteiro"