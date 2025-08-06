import os
import requests
from dotenv import load_dotenv

# Carrega o .env
load_dotenv()

# Pega a chave da API do .env
API_KEY = os.environ.get('API_KEY')

# URL da API com a chave inserida
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# Faz a requisição
try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["result"] == "success":
        print("Cotações baseadas em 1 USD:")
        print(f"Real (BRL): {data['conversion_rates']['BRL']}")
        print(f"Euro (EUR): {data['conversion_rates']['EUR']}")
        print(f"Iene (JPY): {data['conversion_rates']['JPY']}")
        print(f"Libra (GBP): {data['conversion_rates']['GBP']}")
    else:
        print("Erro na API:", data.get("error-type", "Erro desconhecido"))

except Exception as e:
    print("Erro ao acessar a API:", str(e))
