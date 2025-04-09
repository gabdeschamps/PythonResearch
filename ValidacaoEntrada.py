#Validação de Entrada
#Para garantir que o usuário insira um valor válido, você pode usar um loop while com tratamento de exceções:

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

nome = input("Digite seu nome: ")

resultado = numero * 2

print(f"Olá, {nome}! O dobro do número que você digitou é {resultado}.")
