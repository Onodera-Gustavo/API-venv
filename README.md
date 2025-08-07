# 💵 Cotação do Dólar com API ExchangeRate

Este projeto consulta a cotação atual do dólar (USD) em relação ao real (BRL), utilizando a API da ExchangeRate. O script `consulta.py` realiza uma requisição HTTP à API e imprime o valor atualizado no terminal.

---

## ✔️ Requisitos

- Python 3 instalado  
- Ambiente virtual configurado (recomendado)  
- Chave de API da ExchangeRate (definida no arquivo `.env`)

---

## 🚀 Como executar

### 1. Clone o repositório ou baixe os arquivos

```bash
git clone https://github.com/onoderagustavo/API-venv.git
cd API-venv
```

### 2. (Opcional, mas recomendado) Crie e ative um ambiente virtual

```bash
python -m venv venv_seunome
```

- **Windows:**
  ```bash
  venv_seunome\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv_nome/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto (caso ainda não exista) e insira sua chave da API:

```
API_KEY=sua_chave_aqui
```

> ⚠️ **Importante:** Não compartilhe sua chave de API publicamente.

### 5. Execute o script

```bash
python consulta.py
```

O terminal mostrará a cotação atual de 1 dólar em reais.

---

## 📁 Estrutura do Projeto

```
├── consulta.py         # Script principal que realiza a requisição à API
├── requirements.txt    # Lista de dependências
├── .env                # Arquivo de configuração com a chave da API
└── README.md           # Documentação do projeto
```

---

## 🔒 Segurança com .env

O uso do arquivo `.env` ajuda a manter informações sensíveis, como a chave da API, fora do código-fonte. É recomendável adicionar `.env` ao `.gitignore` para evitar o versionamento desse arquivo.

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/). Sinta-se livre para usar, modificar e distribuir conforme necessário.
