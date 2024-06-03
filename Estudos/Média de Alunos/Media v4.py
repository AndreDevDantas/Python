#Calcular Media de X notas de Y alunos

def calcularMedia(notas):
    return round(sum(notas) / len(notas), 1)

def mostrarResultado(aluno, media):
    if media >= 6:
        print(f"Aluno {aluno} foi aprovado com média {media}")
    else:
        print(f"Infelizmente o aluno {aluno} foi reprovado com média {media}")

def finalizarMedias(num_alunos, num_notas):
    medias = []
    for controle in range(1, num_alunos + 1):
        notas = []
        for i in range(1, num_notas + 1):
            nota = float(input(f"Informe a nota {i} do aluno {controle}: "))
            notas.append(nota)
        
        media = calcularMedia(notas)
        medias.append((controle, media))
        mostrarResultado(controle, media)

    print("\nMédia dos Alunos: ")
    for aluno, media in medias:
        print(f"Aluno {aluno}: {media}")

num_alunos = int(input("Informe o número de alunos: "))
num_notas = int(input("Informe o número de notas que irão compor a média: "))
finalizarMedias(num_alunos, num_notas)
