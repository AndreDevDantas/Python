# Calcular média de duas notas de um aluno

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2

if (media < 7):
    print(f"Reprovado com média {media}")
elif (media < 8):
    print(f"Passou raspando com média {media}")
else: 
    print(f"Passou com louvor com média {media}")
