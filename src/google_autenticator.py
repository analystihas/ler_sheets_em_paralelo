import pickle
import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


class OAuthAuthenticator:

    def __init__(self):
        # Escopos necessários
        self.SCOPES = ['https://www.googleapis.com/auth/drive.file']
        

    def autenticar_oauth(self, caminho_credenciais_json):
        """Autentica usando OAuth2 e retorna as credenciais"""
        creds = None
        
        # O arquivo token.pickle armazena os tokens de acesso e refresh do usuário
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        # Se não há credenciais válidas, faz o login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("Atualizando token expirado...")
                creds.refresh(Request())
            else:
                print("Iniciando processo de autenticação...")
                print("Uma janela do navegador será aberta para você fazer login.")
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    caminho_credenciais_json, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Salva as credenciais para a próxima execução
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
                print("Token salvo em token.pickle")
        
        return creds
