from general_helpers import Helpers
from google_autenticator import OAuthAuthenticator
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from dotenv import load_dotenv

helpers = Helpers()
autenticator = OAuthAuthenticator()


import os
import mimetypes
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build

def upload_arquivos_para_drive(caminho_pasta_local, caminho_credenciais_json, pasta_drive_id=None, convert_to_sheets=True):
    """
    Faz upload de todos os arquivos de uma pasta local para o Google Drive.
    Se convert_to_sheets=True, converte arquivos (csv, xls, xlsx, ods) para Google Sheets
    e remove a extensão no nome final do arquivo enviado.
    """
    # Autentica
    credenciais = autenticator.autenticar_oauth(caminho_credenciais_json)
    servico = build('drive', 'v3', credentials=credenciais)

    arquivos_enviados = []

    formatos_convertiveis = ('.csv', '.xls', '.xlsx', '.ods', '.xlsm')

    for nome_arquivo in os.listdir(caminho_pasta_local):
        caminho_completo = os.path.join(caminho_pasta_local, nome_arquivo)
        if not os.path.isfile(caminho_completo):
            continue

        print(f"Enviando: {nome_arquivo}")

        # Extensão
        nome, ext = os.path.splitext(nome_arquivo)
        should_convert = convert_to_sheets and ext.lower() in formatos_convertiveis

        # MIME original
        source_mime, _ = mimetypes.guess_type(caminho_completo)
        if source_mime is None:
            source_mime = 'application/octet-stream'

        # Se for converter → remove extensão do nome
        nome_para_drive = nome if should_convert else nome_arquivo

        # Metadados
        metadados = {'name': nome_para_drive}
        if pasta_drive_id:
            metadados['parents'] = [pasta_drive_id]

        if should_convert:
            metadados['mimeType'] = 'application/vnd.google-apps.spreadsheet'
            print(" → Convertendo para Google Sheets (extensão removida).")

        try:
            media = MediaFileUpload(caminho_completo, mimetype=source_mime, resumable=True)

            arquivo = servico.files().create(
                body=metadados,
                media_body=media,
                fields='id, name, webViewLink'
            ).execute()

            arquivos_enviados.append({
                'nome': arquivo.get('name'),
                'id': arquivo.get('id'),
                'link': arquivo.get('webViewLink')
            })

            print(f"✓ {nome_para_drive} enviado. ID: {arquivo.get('id')}")
        except Exception as e:
            print(f"✗ Erro ao enviar {nome_arquivo}: {e}")

    return arquivos_enviados



# Exemplo de uso
if __name__ == "__main__":
    # Carrega as variáveis do arquivo .env
    load_dotenv()
    
    # Lê as variáveis de ambiente
    PASTA_LOCAL = f"src/{os.getenv('PASTA_COM_DADOS')}"
    CREDENCIAIS_JSON = os.getenv('CREDENCIAIS_JSON')
    LINK_GDRIVE = os.getenv('LINK_GDRIVE')
    
    # Extrai o ID da pasta do link
    PASTA_DRIVE_ID = helpers.extrair_id_pasta_drive(LINK_GDRIVE)
    
    print(f"Pasta local: {PASTA_LOCAL}")
    print(f"ID da pasta Drive: {PASTA_DRIVE_ID}")
    print("\nIniciando upload de arquivos...")
    
    resultados = upload_arquivos_para_drive(PASTA_LOCAL, CREDENCIAIS_JSON, PASTA_DRIVE_ID)
    
    print(f"\n{len(resultados)} arquivo(s) enviado(s) com sucesso!")
    for arquivo in resultados:
        print(f"  - {arquivo['nome']}: {arquivo['link']}")