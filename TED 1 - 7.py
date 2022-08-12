hora=int(input("Informe que horas sao"))
minuto=int(input("Informe o minuto"))
segundo=int(input("Informe os segundos"))

horaemmin=hora*60
minutoemseg=minuto*60

minutostotais=horaemmin+minuto

print("Ate o momento ja se passaram " + str(minutostotais) + " minutos e " + str(segundo) + " segundos")