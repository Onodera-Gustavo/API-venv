# 💸 Cotação de Moedas com Python

Projeto em Python para consultar a cotação do dólar (USD) em relação a outras moedas, utilizando a ExchangeRate API.  
Foi desenvolvido com boas práticas: variáveis de ambiente (.env), virtualenv, versionamento com Git e organização simples.

---

## 🚀 Como rodar este projeto

1. Acesse o site https://www.exchangerate-api.com/  
   Clique em "Get Free API Key", crie uma conta gratuita e copie sua chave de API.

2. Clone este repositório no seu computador com:  
   git clone https://github.com/seu-usuario/API-venv.git  
   Entre na pasta do projeto com:  
   cd API-venv

3. Crie um ambiente virtual com o comando:  
   python -m venv venv

4. Ative o ambiente virtual:  
   No Windows: venv\Scripts\activate  
   No Linux/macOS: source venv/bin/activate

5. Instale as dependências necessárias com:  
   pip install -r requirements.txt

6. Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:  
   API_KEY=sua_chave_aqui  
   (Substitua "sua_chave_aqui" pela chave real que você obteve no passo 1)

7. Execute o programa com o comando:  
   python consulta.py

O terminal exibirá a cotação do dólar em relação ao real (BRL), euro (EUR), libra esterlina (GBP) e iene japonês (JPY).

---

## 📁 Arquivos importantes

- `consulta.py`: Script principal do projeto.
- `.env.example`: Modelo do arquivo `.env`, não contém chave.
- `.gitignore`: Configurado para ignorar o `.env`, `venv/` e caches.
- `requirements.txt`: Lista de dependências do projeto.

---

Projeto simples, prático e útil para treinar consumo de APIs e boas práticas com Python. ✅
