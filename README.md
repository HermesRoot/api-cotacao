# 🌎 API de Cotações  

API que fornece cotações atualizadas de moedas como **USD, EUR, BTC, GBP, JPY, CNY, ARS e CAD** em relação ao BRL.  
Os dados são obtidos da [AwesomeAPI](https://docs.awesomeapi.com.br/) e armazenados em cache para reduzir requisições desnecessárias.  

---

## 🛠️ Tecnologias  
- **🐍 Python** → Linguagem principal  
- **🔥 Flask** → Framework para a API  
- **🌍 Flask-CORS** → Permite acesso de diferentes origens  
- **🌐 Requests** → Realiza requisições à API de cotações  

---

## 🚀 Como Usar  

### 📡 **Endpoints**  

#### 🔹 `GET /cotacao`  
Retorna as cotações das moedas armazenadas no cache.  

**Exemplo de resposta:**  
```json
{
    "USD": {
        "cotacao": 4.97,
        "variacao": 0.25,
        "data": "2025-02-26 12:30:00"
    },
    "EUR": {
        "cotacao": 5.42,
        "variacao": -0.10,
        "data": "2025-02-26 12:30:00"
    }
}
```

---

## 🔧 Como Executar Localmente  

1. **Clone este repositório:**  
   ```sh
   git clone https://github.com/HermesRoot/api-cotacao.git
   cd api-cotacao
   ```

2. **Instale as dependências:**  
   ```sh
   pip install flask flask-cors requests
   ```

3. **Inicie a API:**  
   ```sh
   python cotacao_api.py
   ```

A API estará disponível em **http://127.0.0.1:5000/cotacao**.  

---

## 🌍 **Hospedagem em Produção**  

Para rodar a API em produção, recomenda-se usar **Gunicorn**:  
```sh
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 cotacao_api:app
```

Se for hospedar no **Railway, Render ou Heroku**, basta criar um `Procfile`:  
```txt
web: gunicorn -w 4 -b 0.0.0.0:$PORT cotacao_api:app
```

---

## ⏳ Atualização Automática  

A API busca novas cotações a cada **5 minutos** automaticamente e armazena em um arquivo JSON local.  

---

## 📝 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Desenvolvido por **HermesRoot**.  
