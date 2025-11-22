from faker import Faker
import pandas as pd
import os
import uuid

class GerarTabelas:
    """ Classe para gerar tabelas fictícias com dados aleatórios."""
    def __init__(self, pasta_destino: str = 'data'):
        self.n_tabelas = None
        self.n_linhas = None
        self.pasta_destino = f"src/{pasta_destino}"

    def gerar_tabela(self):
        fake = Faker('pt_BR')
        dados = []
        for _ in range(self.n_linhas):
            linha = {
                'Nome': fake.name(),
                'sobrenome': fake.last_name(),
                'cidade': fake.city(),
                'estado': fake.estado_sigla(),
                'data': fake.date_this_decade().isoformat(),
                'cor_favorita': fake.color_name()
            }
            dados.append(linha)
        return pd.DataFrame(dados)

    def gerar_varias_tabelas(self):
        tabelas = {}
        for _ in range(self.n_tabelas):
            nome_tabela = f"tabela_{uuid.uuid4().hex}"
            tabelas[nome_tabela] = self.gerar_tabela()
        return tabelas


    def salvar_tabelas_csv(self, n_tabelas:int=1, n_linhas:int=100):
        os.makedirs(self.pasta_destino, exist_ok=True)

        self.n_tabelas = n_tabelas
        self.n_linhas = n_linhas

        tabelas = self.gerar_varias_tabelas()
        
        for nome_tabela, df in tabelas.items():
            caminho_arquivo = f'{self.pasta_destino}/{nome_tabela}.csv'
            df.to_csv(caminho_arquivo, index=False)
    
        print(f'{self.n_tabelas} tabelas salvas em {self.pasta_destino}.')

pasta_destino = 'data'

gerar_tabelas = GerarTabelas(pasta_destino=pasta_destino)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gerar tabelas fictícias e salvar em CSV.")

    parser.add_argument("--tabelas", type=int, default=1, help="Número de tabelas a gerar.")
    parser.add_argument("--linhas", type=int, default=100, help="Número de linhas por tabela.")
    parser.add_argument("--destino", type=str, default="data", help="Pasta de destino dos CSVs.")

    args = parser.parse_args()

    gerador = GerarTabelas(pasta_destino=args.destino)
    gerador.salvar_tabelas_csv(n_tabelas=args.tabelas, n_linhas=args.linhas)


# uv run src/gerar_tabelas.py --tabelas 50 --linhas 2000 --destino data
# uv run src/gerar_tabelas.py --tabelas 50 --linhas 5000 --destino data