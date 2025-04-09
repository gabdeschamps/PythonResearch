# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Adicionando elementos
lista.append(6)
print(lista)  # Saída: [1, 2, 3, 4, 5, 6]

# Removendo elementos
lista.remove(2)
print(lista)  # Saída: [1, 3, 4, 5, 6]

# Acessando elementos
print(lista[0])  # Saída: 1
print(lista[-1])  # Saída: 6

# Iterando sobre uma lista
for elemento in lista:
    print(elemento)