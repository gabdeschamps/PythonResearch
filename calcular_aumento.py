def main():
    # Solicitar a idade do usuário
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    # Solicitar o nome do usuário
    nome = input("Digite seu nome: ")

    # Solicitar o salário do usuário
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o salário.")

    # Calcular um aumento de 10%
    aumento = salario * 0.10
    novo_salario = salario + aumento

    # Exibir os resultados
    print(f"\nResumo dos Dados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Salário atual: R${salario:.2f}")
    print(f"Salário com aumento de 10%: R${novo_salario:.2f}")

if __name__ == "__main__":
    main()
