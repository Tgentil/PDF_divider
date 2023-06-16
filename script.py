"""PDF divider"""
import os
from PyPDF2 import PdfReader, PdfWriter


def dividir_pdf(caminho_pasta):
    """
    Divide um arquivo PDF em vários arquivos PDF de uma única página.

    Parâmetros:
        caminho_pasta (str): O caminho completo para a pasta contendo os arquivos PDF.
    """

    # Caminho de saída para os PDFs divididos
    pasta_saida = os.path.join(os.getcwd(), "out")
    os.makedirs(pasta_saida, exist_ok=True)

    # Listar todos os arquivos na pasta
    arquivos_pdf = [arquivo for arquivo in os.listdir(
        caminho_pasta) if arquivo.lower().endswith(".pdf")]

    # Iterar sobre os arquivos PDF
    for arquivo_pdf in arquivos_pdf:
        caminho_pdf = os.path.join(caminho_pasta, arquivo_pdf)

        # Carregar o arquivo PDF
        pdf = PdfReader(caminho_pdf)

        # Obter o nome do arquivo sem a extensão
        nome_arquivo = os.path.splitext(arquivo_pdf)[0]

        # Dividir o PDF em páginas individuais
        for pagina_numero, pagina in enumerate(pdf.pages, start=1):
            pdf_dividido = PdfWriter()
            pdf_dividido.add_page(pagina)

            # Salvar a página em um arquivo PDF separado
            caminho_saida = os.path.join(
                pasta_saida, f"{nome_arquivo}_{pagina_numero}.pdf")
            with open(caminho_saida, "wb") as arquivo_saida:
                pdf_dividido.write(arquivo_saida)

    print("PDFs divididos com sucesso!")


# Caminho para a pasta contendo os arquivos PDF
caminho_da_pasta = os.path.join(os.getcwd(), "data")

# Chamar a função para dividir os PDFs
dividir_pdf(caminho_da_pasta)
