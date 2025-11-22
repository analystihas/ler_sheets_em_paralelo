```md
<p align="center">
  <img src="https://svg-banners.vercel.app/api?type=origin&text1=Leitura%20de%20Múltiplos%20Google%20Sheets%20📄&text2=Python%20•%20Drive%20API%20•%20Paralelismo" width="100%" />
</p>
```

---

# 📚 **Sumário**

```md
## 📚 Sumário

- [📄 Leitura de Múltiplos Google Sheets em Python](#-leitura-de-múltiplos-google-sheets-em-python)
  - [🔄 Comparação entre Leitura Sequencial e com Paralelismo](#-comparação-entre-leitura-sequencial-e-com-paralelismo)
- [🚀 Guia Rápido (Fast Track)](#-guia-rápido-fast-track)
- [📦 Dependências e Ambiente](#-dependências-e-ambiente)
  - [1️⃣ Instalar o uv](#1️⃣-instalar-o-uv)
- [📥 Clonar o Repositório](#-clonar-o-repositório)
- [📦 Instalar as Dependências](#-instalar-as-dependências)
- [🔐 Criar Projeto no Google Cloud + OAuth 20](#-criar-projeto-no-google-cloud--oauth-20)
- [⚙️ Configurar o env](#️-configurar-o-env)
- [🧪 Geração de Dados Fake](#-geração-de-dados-fake)
- [▶️ Como Usar — Linha de Comando](#️-como-usar--linha-de-comando)
- [🔧 Parâmetros dos Scripts](#-parâmetros-dos-scripts)
- [🧩 Arquitetura do Projeto](#-arquitetura-do-projeto)
- [📌 Licença](#-licença)
```

---

# 📄 **Leitura de Múltiplos Google Sheets em Python**

### 🔄 Comparação entre Leitura Sequencial e com Paralelismo

Este projeto demonstra como:

* 🔧 **Gerar tabelas fake**
* ☁️ **Enviar CSVs para o Google Drive**
* 🔀 **Converter CSV → Google Sheets**
* 📂 **Listar todas as planilhas enviadas**
* ⚡ **Comparar leitura sequencial vs paralela** para medir performance

Ideal para estudos, automação e testes de benchmarks com APIs do Google.

---

# 🚀 **Guia Rápido (Fast Track)**

### **0. Instalar dependências**

```bash
uv sync
```

### **1. Gerar 48 tabelas fake (1500 linhas cada)**

```bash
uv run src/gerar_tabelas.py --tabelas 48 --linhas 1500 --destino data
```

### **2. Converter CSVs → Google Sheets e enviar ao Drive**

```bash
uv run src/enviar_para_pasta_no_drive.py
```

### **3. Listar os Sheets enviados**

```bash
uv run src/listar_planilhas.py
```

### 📓 *Notebook principal*

* `seq_vs_paralel.ipynb` → leitura **sequencial vs paralela**

---

# 📦 **Dependências e Ambiente**

O projeto utiliza **uv** como gerenciador de ambiente e dependências.

## 1️⃣ Instalar o `uv`

### Linux / macOS

```bash
curl -fsSL https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
iwr https://astral.sh/uv/install.ps1 -useb | iex
```

Verificar:

```bash
uv --version
```

---

# 📥 **Clonar o Repositório**

```bash
git clone https://github.com/analystihas/ler_sheets_em_paralelo.git
cd ler_sheets_em_paralelo
```

---

# 📦 **Instalar as Dependências**

```bash
uv sync
```

Isso irá:

* criar `.venv`
* instalar dependências do `pyproject.toml`
* preparar ambiente para execução

---

# 🔐 **Criar Projeto no Google Cloud + Gerar Credenciais OAuth 2.0**

Siga o **Tópico 2** deste guia completo no Medium:

[![Ler no Medium](https://img.shields.io/badge/LER%20NO%20MEDIUM-12100E?style=for-the-badge\&logo=medium\&logoColor=white)](https://medium.com/@ihascional/lendo-múltiplos-sheets-com-python-looping-normal-vs-paralelismo-9074a38ce6a8)

### ✔️ **APIs necessárias**

* **Google Drive API**
* **Google Sheets API**
* Criar **OAuth Client ID** no formato *Desktop App*
* Baixar credencial JSON

---

# ⚙️ **Configurar o `.env`**

Crie um arquivo `.env`:

```ini
PASTA_COM_DADOS="data"
CREDENCIAIS_JSON="C:\Users\DELL\OneDrive\Documents\credentials\segredo.json"
LINK_GDRIVE="https://drive.google.com/drive/folders/abcdefghijh?usp=drive_link"
```

### **Descrição dos parâmetros**

| Variável           | Função                                |
| ------------------ | ------------------------------------- |
| `PASTA_COM_DADOS`  | Pasta onde os CSVs fake serão gerados |
| `CREDENCIAIS_JSON` | Caminho da credencial OAuth           |
| `LINK_GDRIVE`      | Pasta destino no Drive                |

---

# 🧪 **Geração de Dados Fake (Simulação e Performance)**

Esta funcionalidade gera tabelas grandes para simular múltiplos sheets e testar paralelismo.

O script:

* usa `Faker` para gerar dados realistas
* cria `N` tabelas com `M` linhas
* salva em CSV
* nomes únicos via UUID

Exemplo:

```
tabela_3f1c8b2e9a9440cfa4b2e88ef0d8c6fb.csv
```

---

# ▶️ **Como Usar — Linha de Comando**

Gerar 48 tabelas (1500 linhas cada):

```bash
uv run src/gerar_tabelas.py --tabelas 48 --linhas 1500 --destino data
```

Gerar 52 tabelas (5000 linhas cada):

```bash
uv run src/gerar_tabelas.py --tabelas 52 --linhas 5000 --destino data
```

---

# 🔧 **Parâmetros dos Scripts**

| Parâmetro   | Tipo | Default | Descrição                  |
| ----------- | ---- | ------- | -------------------------- |
| `--tabelas` | int  | 1       | Quantidade de tabelas fake |
| `--linhas`  | int  | 100     | Linhas por tabela          |
| `--destino` | str  | data    | Pasta destino dos CSVs     |

---

# 🧩 **Arquitetura do Projeto**

| Script                          | Função                               |
| ------------------------------- | ------------------------------------ |
| `gerar_tabelas.py`              | Gera CSVs fake                       |
| `enviar_para_pasta_no_drive.py` | Converte CSV → Google Sheet + Upload |
| `listar_planilhas.py`           | Lista arquivos enviados              |
| `seq_vs_paralel.ipynb`          | Benchmark sequencial vs paralelismo  |

---

# 📌 **Licença**

Uso livre para estudos, benchmarks e automações com dados fictícios.

---