import google.generativeai as genai
from fetch_price import get_eth_data
from fetch_news import get_eth_news

# Configure sua chave da API Gemini (obtenha-a pelo Google AI Studio/MakerSuite)
genai.configure(api_key="AIzaSyBAL2Lpp7a0TKvKyfRPm9Rmupsskoo7qfI")
def gerar_tendencia_24h():
    eth_data = get_eth_data()
    headlines = get_eth_news()

    if not eth_data:
        return "Erro ao obter dados do Ethereum."

    prompt = (
        f"Você é um analista financeiro de criptomoedas. Com base nos dados e nas notícias a seguir, diga se a tendência do Ethereum nas próximas 24 horas é de 'Alta' ou 'Baixa'. "
        f"Seja objetivo e baseie sua resposta nos dados e no sentimento do mercado.\n\n"
        f"Preço atual: ${eth_data['price']}\n"
        f"Volume 24h: ${eth_data['volume']}\n"
        f"Variação 24h: {eth_data['change_24h']}%\n\n"
        f"Últimas manchetes:\n" +
        "\n".join([f"- {h}" for h in headlines]) +
        "\n\nResponda com: Alta ou Baixa, seguida de uma justificativa curta."
    )

    try:
        # Atualizado: usando o modelo "gemini-2.0-flash", que é suportado
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Erro ao gerar análise: {e}"

if __name__ == "__main__":
    resultado = gerar_tendencia_24h()
    print("Tendência do dia:", resultado)
