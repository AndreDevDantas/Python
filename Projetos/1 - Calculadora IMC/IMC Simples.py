#Projeto de Calculadora de IMC em Python Simples
#IMC = Peso/(Altura*Altura)

peso = input("Informe seu peso: ")
altura = input("Informe sua Altura (Use ponto para casas decimais): ")

peso = float(peso)
altura = float(altura)

imc = peso / (altura ** 2)
print(imc)

print(f"seu imc é de {round(imc,2)}")