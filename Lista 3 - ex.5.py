
i=0
par=0
impar=0

while i < 10:
    numeros = int(input("Digite 10 numeros "))
    if (numeros%2)==0:
        par=par+1
    else:
        impar=impar+1
    i=i+1   

print("Há " + str(par) + "numeros pares e " + str(impar) + "numeros impares" )