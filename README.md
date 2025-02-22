# api-cotacao
API de cotação de moedas (USD, EUR, BTC) atualizada a cada 5 minutos.

Aqui está um README básico para sua API de cotações:  

---

# API de Cotações  

Esta é uma API que fornece cotações atualizadas de moedas como USD, EUR e BTC em relação ao BRL. Os dados são obtidos da [AwesomeAPI](https://docs.awesomeapi.com.br/) e armazenados em cache para reduzir requisições desnecessárias.  

## 🔧 Tecnologias  
- Python  
- Flask  
- Flask-CORS  
- Requests  

## 🚀 Como usar  

### 🔹 Endpoints  

#### `GET /cotacao`  
Retorna as cotações das moedas armazenadas.  

### 🔹 Executando localmente  

1. Clone este repositório:  
   ```sh
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Instale as dependências:  
   ```sh
   pip install flask flask-cors requests
   ```

3. Inicie a API:  
   ```sh
   python api.py
   ```

## 📌 Observação  
Esta API atualiza as cotações a cada 5 minutos automaticamente.  

---

Se precisar de ajustes, me avise! 😊
