import tkinter as tk
from tkinter import filedialog, messagebox
from leitor_pdf import extrair_dados
from regra_negocio import calcular_litros

def selecionar_pdf():
    caminho_pdf = filedialog.askopenfilename(
        title="Selecione o PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if not caminho_pdf:
        return

    try:
        dados = extrair_dados(caminho_pdf)
        total = calcular_litros(dados, "listagem_produtos.xlsx")

        resultado_label.config(text=f"Total de Litros: {total:.2f}")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Criar janela
janela = tk.Tk()
janela.title("Calculadora de Litros")
janela.geometry("400x200")

# Título
titulo = tk.Label(janela, text="Leitor de Pedido PDF", font=("Arial", 14))
titulo.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Selecionar PDF", command=selecionar_pdf)
botao.pack(pady=20)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Rodar app
janela.mainloop()