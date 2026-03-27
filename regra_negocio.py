import pandas as pd

def calcular_litros(dados_pdf, caminho_excel):
    df = pd.read_excel(caminho_excel)

    total_litros = 0

    for item in dados_pdf:
        codigo = int(item["codigo"])
        quantidade = item["quantidade"]

        produto = df[df["CÓDIGO"] == codigo]

        if not produto.empty:
            litros = float(produto.iloc[0]["LITROS"])
            total_litros += quantidade * litros
        else:
            print(f"Código não encontrado: {codigo}")

    return total_litros