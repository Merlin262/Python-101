numero = float(input("Digite os números para a média ou digite -1 para sair "))

numeroMedia = 0 
contador = 0 
numeroMediaF = 0

while numero>-1:
    numeroMedia = float(input("Digite os números para a média "))
    if numeroMedia!=-1:
        numeroMediaF = numeroMediaF+numeroMedia
        contador=contador+1
    else:
        media=numeroMediaF/contador
        print("O valor da média é: " + str(media))
        break
        
        
        



