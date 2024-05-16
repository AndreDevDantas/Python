#Cálculo do IMC com multiplas funções

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

def calculoIMC(peso = 0, altura = 0):
    return peso / (altura ** 2)

def resultadoIMC(imc):
    if imc <= 18.5 : return "magreza"
    elif imc <= 24.9 : return "Ideal"
    elif imc <= 29.9 : return "Sobrepeso"
    elif imc <= 39.9 : return "Obesidade"
    else: return "Obesidade Grave"

imc = calculoIMC(peso = peso, altura = altura)
print(resultadoIMC(imc))
