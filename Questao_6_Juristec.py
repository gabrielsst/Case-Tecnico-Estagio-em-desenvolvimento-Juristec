from __future__ import annotations

from io import StringIO

import pandas as pd
from playwright.sync_api import sync_playwright

import unicodedata
from typing import Any, Dict, List, Tuple



def coletar_dados_inmet(codigo_estacao: str) -> Dict[str, Tuple[float, int]]:
    url = f"https://tempo.inmet.gov.br/TabelaEstacoes/{codigo_estacao.upper()}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_selector("table", timeout=60000)

        tabela_html = page.locator("table").evaluate("el => el.outerHTML")
        browser.close()

    df = pd.read_html(StringIO(tabela_html), header=[0, 1])[0]

    # Achata o cabeçalho de múltiplos níveis em uma string única
    colunas = []
    for col in df.columns:
        if isinstance(col, tuple):
            nome = " ".join(str(parte).strip() for parte in col if str(parte) != "nan")
        else:
            nome = str(col).strip()
        colunas.append(" ".join(nome.split()))

    df.columns = colunas

    # Encontra as colunas corretas sem depender do nome exato
    col_hora = None
    col_temp = None
    col_umid = None

    for col in df.columns:
        texto = col.lower()

        if "hora" in texto and "utc" in texto:
            col_hora = col
        elif "temperatura" in texto and "inst" in texto:
            col_temp = col
        elif "umidade" in texto and "inst" in texto:
            col_umid = col

    if not col_hora or not col_temp or not col_umid:
        raise ValueError(
            f"Não foi possível localizar as colunas esperadas. Colunas encontradas: {df.columns.tolist()}"
        )

    df = df[[col_hora, col_temp, col_umid]].copy()
    df.columns = ["hora", "temperatura", "umidade"]

    df = df.dropna(subset=["hora", "temperatura", "umidade"])

    # --- HORA ---
    df["hora"] = (
        df["hora"]
        .astype(str)
        .str.extract(r"(\d{1,4})", expand=False)  # pega números
        .str.zfill(4)  # garante 4 dígitos (0000, 0100...)
        .apply(lambda x: f"{x[:2]}:{x[2:]}")
    )

    # --- TEMPERATURA ---
    df["temperatura"] = (
    df["temperatura"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
    / 10
    )

    # --- UMIDADE ---
    df["umidade"] = (
        df["umidade"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
        / 10
    )

    resultado = {}
    for _, row in df.iterrows():
        resultado[row["hora"]] = (row["temperatura"], row["umidade"])

    return resultado

def _normalizar_texto(texto: str) -> str:
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(texto.split())


def buscar_estacoes_operantes(municipio: str, uf: str) -> List[Dict[str, Any]]:
    url = "https://portal.inmet.gov.br/paginas/catalogoaut"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=60000)

        page.wait_for_selector("table", timeout=60000)
        tabela_html = page.locator("table").evaluate("el => el.outerHTML")

        browser.close()

    tabelas = pd.read_html(StringIO(tabela_html))
    if not tabelas:
        raise ValueError("Nenhuma tabela foi encontrada na página do catálogo.")

    df = tabelas[0].copy()
    df.columns = [str(col).strip() for col in df.columns]

    col_nome = "Nome"
    col_uf = "UF"
    col_situacao = "Situação"

    if col_nome not in df.columns or col_uf not in df.columns or col_situacao not in df.columns:
        raise ValueError(f"Colunas esperadas não encontradas. Colunas atuais: {df.columns.tolist()}")

    municipio_norm = _normalizar_texto(municipio)
    uf_norm = _normalizar_texto(uf)

    df["_nome_norm"] = df[col_nome].apply(_normalizar_texto)
    df["_uf_norm"] = df[col_uf].apply(_normalizar_texto)
    df["_situacao_norm"] = df[col_situacao].apply(_normalizar_texto)

    filtrado = df[
        df["_nome_norm"].str.contains(municipio_norm, na=False)
        & df["_uf_norm"].str.contains(uf_norm, na=False)
        & (df["_situacao_norm"] == "operante")
    ].copy()

    filtrado = filtrado.drop(columns=["_nome_norm", "_uf_norm", "_situacao_norm"])

    return filtrado["Código"].dropna().unique().tolist()


if __name__ == "__main__":
    # buscar_estacoes_operantes("Estação_que_deseja", "UF_que_deseja") <- Trocar a estação e UF na função
    resultados = buscar_estacoes_operantes("Brasília", "DF")
    for resultado in resultados:
      dados = coletar_dados_inmet(resultado)
      print(dados)