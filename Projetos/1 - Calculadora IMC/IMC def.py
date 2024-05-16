#Projeto de Calculadora de IMC em Python com Def
#IMC = Peso/(Altura*Altura)

Peso = input("Informe seu Peso: ")
Altura = input("Informe sua altura (use . para casas decimais): ")

def calcular_imc(Peso = 0, Altura = 0):
    imc = float(Peso) / (float(Altura) ** 2)
    return round(imc, 1)

imc = calcular_imc(Peso = Peso, Altura = Altura)
if imc < 16.9:
    print("Muito abaixo do Peso.")
elif imc < 18.4:
    print("Abaixo do Peso.")
elif imc < 24.9:
    print("Peso Ideal.")
elif imc < 29.9:
    print("Acima do Peso.")
elif imc < 34.9:
    print("Obesidade Grau I.")
elif imc < 40:
    print("Obesidade Grau II.")
else:
    print("Obesidade Grau III.")