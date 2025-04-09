# Criando um dicionário
aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Engenharia"
}

# Acessando valores
print(aluno["nome"])  # Saída: Maria

# Adicionando novos pares
aluno["cidade"] = "São Paulo"

# Iterando sobre um dicionário
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
