
# 📄 Leitura de Múltiplos Google Sheets em Python

### Comparação entre Leitura Normal e Leitura com Paralelismo

Este projeto demonstra como **gerar tabelas fake**, **enviar para o Google Drive**, **convertê-las em Google Sheets**, **listar arquivos**, e principalmente como **ler múltiplos sheets usando abordagem sequencial vs. paralela** para avaliar ganho de performance.

---

# 🚀 Guia Rápido (Fast Track)

```bash
# 1. Gerar 48 tabelas fake
uv run src/gerar_tabelas.py --tabelas 48 --linhas 1500 --destino data

# 2. Converter CSVs em Google Sheets e enviar para o Drive
uv run src/enviar_para_pasta_no_drive.py

# 3. Listar os Sheets enviados para o Drive
uv run src/listar_planilhas.py
```

Notebook para testes:

* `extract_simples.ipynb` → leitura sequencial dos Sheets
* `paralelo.ipynb` → leitura paralela dos Sheets

---

# 📦 Dependências e Ambiente

O projeto utiliza o **uv** como gestor de ambiente e dependências.

## 1. Instalar o `uv`

### Linux/macOS

```bash
curl -fsSL https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
iwr https://astral.sh/uv/install.ps1 -useb | iex
```

Verificar instalação:

```bash
uv --version
```

---

# 📥 2. Clonar o Repositório

```bash
git clone https://github.com/analystihas/ler_sheets_em_paralelo.git
cd ler_sheets_em_paralelo
```

---

# 📦 3. Instalar as Dependências

```bash
uv sync
```

Isso irá:

* criar `.venv`
* instalar dependências do `pyproject.toml`
* deixar o projeto pronto para execução

---

# 🔐 4. Criar Projeto no Google Cloud e Gerar Credenciais OAuth 2.0

Siga o **tópico 2** deste guia no Medium:
[https://medium.com/p/9074a38ce6a8/edit](https://medium.com/p/9074a38ce6a8/edit)

Você precisará permitir acesso às APIs:

### ✔️ APIs necessárias

* **Google Drive API**
* **Google Sheets API**
* **OAuth 2.0 Client ID** configurado como *Desktop App*
* Download da credencial JSON (cliente OAuth)

---

# ⚙️ 5. Configurar o `.env`

Crie um arquivo `.env` na raiz do projeto:

```ini
PASTA_COM_DADOS="data"
CREDENCIAIS_JSON="C:\Users\DELL\OneDrive\Documents\credentials\segredo.json"
LINK_GDRIVE="https://drive.google.com/drive/folders/abcdefghijh?usp=drive_link"
```

Descrição:

* **PASTA_COM_DADOS**: onde os CSVs gerados serão salvos
* **CREDENCIAIS_JSON**: caminho para seu arquivo OAuth
* **LINK_GDRIVE**: pasta destino no Google Drive

---

# 🧪 Geração de Dados Fake (para testes de performance)

Esta funcionalidade apenas simula tabelas grandes para avaliar a diferença entre leitura sequencial e paralela.

O script:

* gera dados realistas com `Faker`
* cria quantas tabelas você desejar
* salva tudo em `.csv`
* cada arquivo recebe um nome único (UUID), ex:

```
tabela_3f1c8b2e9a9440cfa4b2e88ef0d8c6fb.csv
```

---

# ▶️ Como Usar — Linha de Comando

Exemplo: gerar 48 tabelas com 1500 linhas:

```bash
uv run src/gerar_tabelas.py --tabelas 48 --linhas 1500 --destino data
```

Outro exemplo: gerar 52 tabelas com 5000 linhas:

```bash
uv run src/gerar_tabelas.py --tabelas 52 --linhas 5000 --destino data
```

---

# 🔧 Parâmetros dos Scripts

| Parâmetro   | Tipo | Default | Descrição                       |
| ----------- | ---- | ------- | ------------------------------- |
| `--tabelas` | int  | 1       | Quantidade de tabelas a gerar   |
| `--linhas`  | int  | 100     | Linhas por tabela               |
| `--destino` | str  | data    | Pasta onde os CSVs serão salvos |

---

# 🧩 Arquitetura do Projeto

### Scripts principais

| Script                          | Função                                             |
| ------------------------------- | -------------------------------------------------- |
| `gerar_tabelas.py`              | Gera CSVs fake para testes                         |
| `enviar_para_pasta_no_drive.py` | Converte CSV → GSheet e envia ao Drive             |
| `listar_planilhas.py`           | Lista todos os Sheets da pasta                     |
| `seq_vs_paralel.ipynb`          | Leitura sequencial  vs paralela                    |


---

# 📌 Licença

Uso livre para estudos, benchmarks e testes com dados fictícios.
