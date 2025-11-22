class Helpers:

    @staticmethod
    def extrair_id_pasta_drive(link_drive):
        """Extrai o ID da pasta do link do Google Drive"""
        if '/folders/' in link_drive:
            return link_drive.split('/folders/')[1].split('?')[0]
        return link_drive  # Retorna o próprio valor se já for um ID
    
