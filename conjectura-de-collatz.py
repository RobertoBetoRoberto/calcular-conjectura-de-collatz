print("Digite até qual número você deseja testar")
    
NP1 = 0
NP2 = 0
NP3 = 0
NP4 = 0
NP5 = 0
N1 = 0
N2 = 0
N3 = 0
N4 = 0
N5 = 0

while True:
    quantidade_testes = int(input())
    if quantidade_testes > 2:
        break
    print("Números negativos, menores ou iguais a 2 não são validos. Por favor digite um número positivo maior que 1.")

for i in range (2, quantidade_testes + 1):
    print(f"Teste do número: {i}\n")
    numero = i
    passos = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
            print(numero)
            passos += 1
        else:
            numero = (numero * 3) + 1
            print(numero)
            passos += 1
    if passos > NP1:
        NP5 = NP4
        N5 = N4
        NP4 = NP3
        N4 = N3
        NP3 = NP2
        N3 = N2
        NP2 = NP1
        N2 = N1
        NP1 = passos
        N1 = i
    elif passos > NP2:
        NP5 = NP4
        N5 = N4
        NP4 = NP3
        N4 = N3
        NP3 = NP2
        N3 = N2
        NP2 = passos
        N2 = i
    elif passos > NP3:
        NP5 = NP4
        N5 = N4
        NP4 = NP3
        N4 = N3
        NP3 = passos
        N3 = i
    elif passos > NP4:
        NP5 = NP4
        N5 = N4
        NP4 = passos
        N4 = i
    elif passos > NP5:
        NP5 = passos
        N5 = i
    print(f"\nNúmero de passos: {passos}\n \n FIM\n")
print(f"Numeros com maiores quantidades de passos:\n Número: {N1} | Passos: {NP1}\n Número: {N2} | Passos: {NP2}\n Número: {N3} | Passos: {NP3}\n Número: {N4} | Passos: {NP4}\n Número: {N5} | Passos: {NP5} ")
input("FIM DO ALGORITMO")