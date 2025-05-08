import os
import re
import pandas as pd
from google.colab import drive
import fitz  # PyMuPDF
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.colab import auth
from google.colab import files
import google.auth
from io import BytesIO


# Verifica se a biblioteca PyMuPDF está instalada
try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF não está instalado. Instalando agora...")
    os.system("pip install pymupdf")


def extrair_valores_prestacao_servico(pdf_caminho):
    """Extrair valores relacionados à prestação de serviço de um arquivo PDF."""
    documento = fitz.open(pdf_caminho)
    texto = ""
    for pagina in documento:
        texto += pagina.get_text()
    documento.close()

    # Padrões para identificar valores relacionados à prestação de serviço
    padroes = [
        r"(?i)(valor(?:es)?)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Valor (R$)
        r"(?i)(preço(?:s)?)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",   # Preço (R$)
        r"(?i)(serviço(?:s)?)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Serviço (R$)
        r"(?i)(valor bruto total)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Valor bruto total (R$)
        r"(?i)(montante de)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Montante de (R$)
        r"(?i)(montante)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Montante (R$)
        r"(?i)(equivalente a)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Equivalente a (R$)
        r"(?i)(valor total)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Valor total (R$)
        r"(?i)(pagamento de)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # Pagamento de (R$)
        r"(?i)(no valor de)\s*[:\-]?\s*(R\$\s*\d+[.,]?\d{0,2})",  # No valor de (R$)
        r"(?i)(USD)\s*(\d+[.,]?\d{0,2})",  # USD
        r"(R\$\s*\d+[.,]?\d{0,2})",  # Identificar R$
        r"(USD\s*\d+[.,]?\d{0,2})"   # Identificar USD
    ]

    valores = []
    for padrao in padroes:
        correspondencias = re.findall(padrao, texto)
        for correspondencia in correspondencias:
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


# Integração com o Google Drive (somente em ambiente Colab)
try:
    print("Montando o Google Drive...")
    drive.mount('/content/drive')
    print("Google Drive montado com sucesso!")
except Exception as e:
    print(f"Erro ao montar o Google Drive: {e}")


def autenticar_google_drive():
    """Autentica o Google Colab para acessar a API do Google Drive usando OAuth2."""
    auth.authenticate_user()
    creds, _ = google.auth.default()
    service = build('drive', 'v3', credentials=creds)
    return service


def obter_arquivos_drive(folder_id):
    """Busca arquivos de uma pasta do Google Drive usando a API"""
    service = autenticar_google_drive()  # Agora a autenticação ocorre aqui.
    query = f"'{folder_id}' in parents and mimeType = 'application/pdf'"
    resultados = service.files().list(q=query).execute()
    return resultados.get('files', [])

def salvar_pdf_localmente(service, file_id, file_name):
    """Salva um PDF do Google Drive no diretório local."""
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    fh.seek(0)

    with open(f"/content/{file_name}", 'wb') as f:
        f.write(fh.read())

def remover_pdfs(diretorio):
    """Remove todos os arquivos PDF do diretório especificado."""
    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith(".pdf"):
            os.remove(os.path.join(diretorio, arquivo))


if __name__ == "__main__":
    caminho_diretorio = input("Informe o caminho do diretório contendo os arquivos PDF no Google Drive: ")
    
    # Verifica se o caminho fornecido é uma URL do Google Drive
    if caminho_diretorio.startswith("https://drive.google.com/"):
        # Extrair o ID da pasta a partir da URL do Google Drive
        folder_id = caminho_diretorio.split("/")[-1]
        
        # Obter arquivos da pasta no Google Drive usando a API
        arquivos_drive = obter_arquivos_drive(folder_id)
        
        # Salvar PDFs temporariamente no ambiente local
        for arquivo in arquivos_drive:
            file_id = arquivo['id']
            service = autenticar_google_drive()  # Obtenha o serviço para baixar o arquivo.
            request = service.files().get_media(fileId=file_id)
            fh = BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                _, done = downloader.next_chunk()
            fh.seek(0)
            # Salve os arquivos locais
            with open(f"/content/{arquivo['name']}", 'wb') as f:
                f.write(fh.read())

        # Agora, vamos processar os arquivos locais temporários
        caminho_diretorio = "/content"
    # Se não for uma URL, então assume-se que é um caminho local
    else:
        caminho_diretorio = os.path.abspath(caminho_diretorio)

    # Verifique se o diretório existe
    if not os.path.exists(caminho_diretorio):
        print(f"Erro: O diretório '{caminho_diretorio}' não foi encontrado.")
        exit()  # Interrompa o script se o diretório não existir

    # Exiba o caminho para depuração
    print(f"Processando arquivos no diretório: {caminho_diretorio}")
        
    # Processar os arquivos
    resultado_df = extrair_de_diretorio(caminho_diretorio)

    # Exibe e exporta os resultados
    if not resultado_df.empty:
        print(resultado_df)
        # Exporta para Excel
        resultado_df.to_excel("/content/valores_prestacao_servico.xlsx", index=False)
        files.download("/content/valores_prestacao_servico.xlsx")
        print("Resultados exportados para valores_prestacao_servico.xlsx")
    else:
        print("Nenhum valor de prestação de serviço foi encontrado nos PDFs.")

    # Remover os arquivos PDF baixados
    remover_pdfs("/content")
    print("Arquivos PDF removidos do diretório local.")

    # Desmonta o Google Drive após a execução
    try:
        drive.flush_and_unmount()
        print("Acesso ao Google Drive removido com sucesso!")
    except Exception as e:
        print(f"Erro ao desmontar o Google Drive: {e}")
