#Projeto de Calculadora de IMC Simples em Python

peso = input("Informe seu peso: ")
altura = input("Informe sua Altura (Use . para casas decimais): ")

peso = float(peso)
altura = float(altura)
imc = peso / (altura ** 2)

print(f"seu imc é de {round(imc,2)}")