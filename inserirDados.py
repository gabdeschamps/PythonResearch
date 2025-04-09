#Para permitir que o usuário insira dados em um programa Python, você pode usar a função input(). A função input() lê uma linha de entrada do usuário como uma string. Se você precisa de um número (inteiro ou ponto flutuante), você pode converter essa string usando as funções int() ou float().

# Exemplo Simples de Entrada de Dados
# Aqui está um exemplo básico de como solicitar ao usuário que insira um número e uma string, e usar esses dados para realizar um cálculo ou exibir uma mensagem:

# Solicitar um número ao usuário
numero = int(input("Digite um número: "))

# Solicitar uma string ao usuário
nome = input("Digite seu nome: ")

# Realizar um cálculo simples
resultado = numero * 2

# Exibir os resultados
print(f"Olá, {nome}! O dobro do número que você digitou é {resultado}.")
