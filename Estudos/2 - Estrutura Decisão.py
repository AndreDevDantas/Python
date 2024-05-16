#Testando e brincando com estrutura de decisão (If, Else, Elif)

#Brincando com a indentação  para saida do print
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

if a > b:
    print(f"O valor de a = {a} é maior que o valor de b = {b}")
else:
    print(f"O valor de b = {b} é maior que o valor de a = {b}")

print("Aqui vai aparecer sempre")


#testando estrutura em uma linha
print(f"a = {a} < b = {b}") if a < b else print(f"a = {a} > b{b}")


#Brincando com else para opções não planejadas
categoria = int(input("Informe o valor da categoria: "))

if categoria == 1:
    print("Valor 10")
elif categoria == 2:
    print("Valor 20")
else:
    print("Valor não encontrado")