from google_autenticator import OAuthAuthenticator
from googleapiclient.discovery import build
import os
from general_helpers import Helpers
from dotenv import load_dotenv

autenticator = OAuthAuthenticator()

def listar_planilhas_na_pasta(pasta_id, caminho_credenciais_json):
    """
    Lista todas as planilhas (Google Sheets) em uma pasta do Drive.
    
    Args:
        pasta_id: ID da pasta do Google Drive
        caminho_credenciais_json: Caminho das credenciais OAuth2
    
    Returns:
        Lista de dicionários com {id, nome} das planilhas
    """
    
    # Autentica
    creds = autenticator.autenticar_oauth(caminho_credenciais_json)
    
    # Cria o cliente do Drive API
    servico_drive = build('drive', 'v3', credentials=creds)
    
    # Busca por arquivos do tipo Google Sheets na pasta
    query = f"'{pasta_id}' in parents and mimeType='application/vnd.google-apps.spreadsheet' and trashed=false"
    
    resultados = servico_drive.files().list(
        q=query,
        fields="files(id, name)",
        pageSize=100
    ).execute()
    
    planilhas = resultados.get('files', [])
    
    print(f"✓ Encontradas {len(planilhas)} planilha(s) na pasta")

    print(f"{planilhas[0:5]}...]")
    
    return planilhas

if __name__ == "__main__":
    helpers = Helpers()
    load_dotenv()
    LINK_GDRIVE = os.getenv('LINK_GDRIVE')
    CREDENCIAIS_JSON = os.getenv('CREDENCIAIS_JSON')

    pasta_id = helpers.extrair_id_pasta_drive(LINK_GDRIVE)

    listar_planilhas_na_pasta(pasta_id=pasta_id, caminho_credenciais_json=CREDENCIAIS_JSON)
    