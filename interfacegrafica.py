import tkinter as tk
from tkinter import messagebox

def calcular_aumento():
    try:
        # Obter os valores das entradas
        idade = int(entrada_idade.get())
        nome = entrada_nome.get()
        salario = float(entrada_salario.get())

        # Calcular o aumento de 10%
        aumento = salario * 0.10
        novo_salario = salario + aumento

        # Exibir os resultados em uma mensagem
        mensagem = (f"Nome: {nome}\n"
                    f"Idade: {idade} anos\n"
                    f"Salário atual: R${salario:.2f}\n"
                    f"Salário com aumento de 10%: R${novo_salario:.2f}")
        messagebox.showinfo("Resultado", mensagem)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configurar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Aumento de Salário")

# Rótulos e campos de entrada
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Salário:").grid(row=2, column=0, padx=10, pady=5)
entrada_salario = tk.Entry(janela)
entrada_salario.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular o aumento
botao_calcular = tk.Button(janela, text="Calcular Aumento", command=calcular_aumento)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da interface
janela.mainloop()
