texto = input("Digite uma string para inverter: ")
textoi = ""

for i in range(len(texto) - 1, -1, -1):
    textoi += texto[i]

print("String original:", texto)
print("String invertida:", textoi)
 