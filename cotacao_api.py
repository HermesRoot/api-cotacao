import requests
import json
import time
import threading
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/cotacao": {"origins": "*"}})

CACHE_FILE = "cotacoes.json"
UPDATE_INTERVAL = 300  # 5 minutos
API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

def atualizar_cotacoes():
    """Obtém as cotações da AwesomeAPI e salva em um arquivo JSON periodicamente."""
    while True:
        try:
            resposta = requests.get(API_URL)
            print("Resposta da API:", resposta.text)  # Debug para verificar a resposta

            if resposta.status_code == 200:
                dados = resposta.json()
                cotacoes = {
                    "USD": {
                        "cotacao": float(dados["USDBRL"]["bid"]),
                        "variacao": float(dados["USDBRL"]["pctChange"]),
                        "data": dados["USDBRL"]["create_date"]
                    },
                    "EUR": {
                        "cotacao": float(dados["EURBRL"]["bid"]),
                        "variacao": float(dados["EURBRL"]["pctChange"]),
                        "data": dados["EURBRL"]["create_date"]
                    },
                    "BTC": {
                        "cotacao": float(dados["BTCBRL"]["bid"]),
                        "variacao": float(dados["BTCBRL"]["pctChange"]),
                        "data": dados["BTCBRL"]["create_date"]
                    }
                }
                with open(CACHE_FILE, "w") as arquivo:
                    json.dump(cotacoes, arquivo)
                print("Cotações atualizadas com sucesso!")
            else:
                print(f"Erro na API: {resposta.status_code} - {resposta.text}")
        except Exception as e:
            print("Erro ao obter cotações:", e)
        
        time.sleep(UPDATE_INTERVAL)

@app.route("/cotacao", methods=["GET"])
def obter_cotacoes():
    """Retorna as cotações armazenadas no arquivo JSON."""
    try:
        with open(CACHE_FILE, "r") as arquivo:
            dados = json.load(arquivo)
        return jsonify(dados)
    except FileNotFoundError:
        return jsonify({"erro": "Cotações ainda não disponíveis"}), 500

if __name__ == "__main__":
    thread = threading.Thread(target=atualizar_cotacoes, daemon=True)
    thread.start()
    
    app.run(debug=True, host="0.0.0.0", port=5000)
