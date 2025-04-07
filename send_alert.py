import asyncio
from telegram import Bot
from analyze_trend import gerar_tendencia_24h

TELEGRAM_TOKEN = "8176825194:AAFJ_kkeJYD6SQ5h0QD0d94fWkxkptuBN4E"
CHAT_ID = "808807976"

async def enviar_alerta_diario():
    mensagem = gerar_tendencia_24h()
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=f"📊 Tendência do Ethereum (24h):\n{mensagem}")
        print("✅ Alerta enviado com sucesso.")
    except Exception as e:
        print("❌ Erro ao enviar alerta:", e)

if __name__ == "__main__":
    asyncio.run(enviar_alerta_diario())
