import requests

# Pegue uma API key grátis em: https://gnews.io/
GNEWS_API_KEY = "c1ed89ee8426b0c3c164a2d94a4e95e2"

def get_eth_news():
    url = f"https://gnews.io/api/v4/search?q=ethereum&lang=en&max=5&token={GNEWS_API_KEY}"
    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])
        headlines = [article["title"] for article in articles]
        return headlines
    except Exception as e:
        print("Erro ao buscar notícias:", e)
        return []

# Exemplo
if __name__ == "__main__":
    for h in get_eth_news():
        print("-", h)
