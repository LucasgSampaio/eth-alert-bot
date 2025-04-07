from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analyze_trend import gerar_tendencia_24h

TELEGRAM_TOKEN = "8176825194:AAFJ_kkeJYD6SQ5h0QD0d94fWkxkptuBN4E"

async def alerta_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = gerar_tendencia_24h()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"📊 Tendência do Ethereum:\n{resultado}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("alerta", alerta_handler))
    print("🤖 Bot rodando... envie /alerta no Telegram")
    app.run_polling()
