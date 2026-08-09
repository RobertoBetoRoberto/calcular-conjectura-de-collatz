print("Digite um número positivo inteiro maior que 1.")

while True:
    numero = int(input())
    if numero > 1:
        break
    print("Números negativos, menores ou iguais a 1 não são validos. Por favor digite um número positivo maior que 1.")

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
        print(numero)
    else:
        numero = (numero * 3) + 1
        print(numero)
input("FIM")