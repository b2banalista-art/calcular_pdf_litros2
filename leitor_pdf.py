import pdfplumber
import re

def extrair_dados(caminho_pdf):
    dados = []

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            linhas = texto.split("\n")

            codigo_atual = None

            for linha in linhas:
                match_codigo = re.search(r'^(\d{3,})\s+-', linha)
                if match_codigo:
                    codigo_atual = match_codigo.group(1)

                match_qtd = re.search(r'(\d+)\s+PEC/1', linha)
                if match_qtd and codigo_atual:
                    quantidade = int(match_qtd.group(1))

                    dados.append({
                        "codigo": codigo_atual,
                        "quantidade": quantidade
                    })

                    codigo_atual = None

    return dados