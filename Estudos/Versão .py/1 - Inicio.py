#Primeiro Hello World
nome = print("Olá Mundo")
print(nome)


#Teste com Input
nome = input("Informe o nome para ser apresentado: ")
print(nome)


#Testando str e int
x = "1"
y = 1
print(x + str(y))
print(int(x) + y)


#Brincando com tipos de dados
a = 1
b = 1.1
c = True
d = [1, "a", True, {"nome": "André", "idade": 20}]
e = "Bem vindo ao meu código"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(e, e[4], e[0:2], e[-4:-1])

print("O valor de x é %d" %10)
print(f"O valor de x é {10 * 2}")