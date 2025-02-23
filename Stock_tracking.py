#? Theo dõi giá cổ phiếu
import requests
def get_stock_price(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=your_api_key"
    response = requests.get(url)
    data = response.json()
    return data['c']
print(get_stock_price('AAPL'))