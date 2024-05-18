#Calcular Media de duas notas de um aluno
def recolherNotas():
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    return n1, n2

def calcularMedia(n1, n2):
    return (n1 + n2) / 2

def mostrarResultado(media):
    if(media < 6):
        print(f"Reprovado com media {media}")
    elif(media < 8): 
        print(f"Passou raspando com media {media}")
    else: 
        print(f"Parabéns, passou com media {media}")

n1, n2 = recolherNotas()
media = calcularMedia(n1, n2)
mostrarResultado(media)