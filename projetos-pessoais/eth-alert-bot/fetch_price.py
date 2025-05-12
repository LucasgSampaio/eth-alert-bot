import requests

def get_eth_data():
    url = "https://api.coingecko.com/api/v3/coins/ethereum"
    params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false",
        "sparkline": "false"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        price = data["market_data"]["current_price"]["usd"]
        volume = data["market_data"]["total_volume"]["usd"]
        change_24h = data["market_data"]["price_change_percentage_24h"]

        return {
            "price": price,
            "volume": volume,
            "change_24h": change_24h
        }

    except Exception as e:
        print("Erro ao obter dados do Ethereum:", e)
        return None

if __name__ == "__main__":
    eth_data = get_eth_data()
    if eth_data:
        print(f"Preço: ${eth_data['price']}")
        print(f"Volume 24h: ${eth_data['volume']}")
        print(f"Variação 24h: {eth_data['change_24h']}%")
