numeros = int(input("Digite 10 numeros "))

i=0
par=0
impar=0

while i <= 10:
    if (numeros%2):
        par=par+1
    else:
        impar=impar+1
    i=i+1   

print("Há " + str(par) + "numeros pares e " + str(impar) + "numeros impares" )