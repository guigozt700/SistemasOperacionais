binario = input('Numero binário: ')
decimal = 0

indice = len(binario) -1
potencia = 0

while indice >= 0:
    decimal += int(binario[indice]) *  (2**potencia)
    potencia += 1
    indice -= 1

print('Decimal é: ',decimal)