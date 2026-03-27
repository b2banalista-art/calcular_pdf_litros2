import streamlit as st
from leitor_pdf import extrair_dados
from regra_negocio import calcular_litros
import tempfile

st.title("📄 CALCULADORA DE PEDIDO | ANALISTA SAVIO")

arquivo = st.file_uploader("Selecione o PDF", type=["pdf"])

if arquivo is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(arquivo.read())
        caminho_pdf = tmp.name

    dados = extrair_dados(caminho_pdf)
    total = calcular_litros(dados, "listagem_produtos.xlsx")

    st.success(f"Total de litros: {total:.2f}")
