import os
import re
import pandas as pd
import gdown

# Verifica se a biblioteca PyMuPDF está instalada
try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF não está instalado. Instalando agora...")
    os.system("pip install pymupdf")
import re
import pandas as pd


def extrair_valores_prestacao_servico(pdf_caminho):
    """Extrair valores relacionados à prestação de serviço de um arquivo PDF."""
    documento = fitz.open(pdf_caminho)
    texto = ""
    for pagina in documento:
        texto += pagina.get_text()
    documento.close()

    # Padrões para identificar valores relacionados à prestação de serviço
    padroes = [
        r"(?i)(valor(?:es)?|orçamento(?:os)?|preço(?:s)?|serviço(?:s)?):?\s*(R\$\s*\d+[.,]?\d{0,2})",
        r"(R\$\s*\d+[.,]?\d{0,2})\s*(?:pelos?\s+serviços?)"
    ]

    valores = []
    for padrao in padroes:
        correspondencias = re.findall(padrao, texto)
        for correspondencia in correspondencias:
            # Verifica se a correspondência é uma tupla ou string
            valores.append(correspondencia if isinstance(correspondencia, str) else correspondencia[1])

    return valores


def extrair_de_diretorio(diretorio_caminho):
    """Extrair valores de prestação de serviço de todos os PDFs em um diretório especificado."""
    dados = []
    for nome_arquivo in os.listdir(diretorio_caminho):
        if nome_arquivo.lower().endswith(".pdf"):
            caminho_pdf = os.path.join(diretorio_caminho, nome_arquivo)
            valores = extrair_valores_prestacao_servico(caminho_pdf)
            dados.append({"arquivo": nome_arquivo, "valores": valores})

    # Converter para DataFrame para melhor visualização e manipulação
    df = pd.DataFrame(dados)
    return df


# Verifica se a biblioteca PyMuPDF está instalada
try:
    import fitz
except ImportError:
    print("PyMuPDF não está instalado. Instalando agora...")
    os.system("pip install pymupdf")

# Integração com o Google Drive (somente em ambiente Colab)
try:
    from google.colab import drive
    print("Montando o Google Drive...")
    drive.mount('/content/drive')
    print("Google Drive montado com sucesso!")
except ImportError:
    print("Ambiente fora do Colab. Certifique-se de fornecer o caminho completo do Google Drive.")

if __name__ == "__main__":
    caminho_diretorio_drive = input("Informe o caminho do diretório contendo os arquivos PDF no Google Drive: ")

    # Download the files to a local directory
    # Use regex to replace special characters in the url and to ensure no "/" at the end
    caminho_diretorio_local = re.sub('[^a-zA-Z0-9]+', '_', caminho_diretorio_drive)[:-1]
    os.makedirs(caminho_diretorio_local, exist_ok=True)
    gdown.download_folder(url=caminho_diretorio_drive, output=caminho_diretorio_local)
    
    # Update code to use the local directory where the files were downloaded
    resultado_df = extrair_de_diretorio(caminho_diretorio_local)
    print(resultado_df)
    resultado_df.to_csv("valores_prestacao_servico.csv", index=False)
