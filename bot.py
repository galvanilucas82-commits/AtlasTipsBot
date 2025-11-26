import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ATLAS TIPS BOT ATIVO!\n\n"
        "Comandos disponíveis:\n"
        "/jogos – Jogos do dia\n"
        "/resultado – Resultado final\n"
        "/over – Over/Under\n"
        "/escanteios – Escanteios\n"
        "/combo – Combo do dia"
    )

# ---------------- JOGOS ----------------
async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """📅 JOGOS DO DIA – ATLAS TIPS

🇧🇷 Flamengo x Cruzeiro
🇧🇷 Palmeiras x Santos
🇪🇸 Real Madrid x Betis
🇮🇹 Juventus x Milan
🇩🇪 Bayern x Leverkusen

📊 Peça análises:
➡️ /resultado
➡️ /over
➡️ /escanteios
➡️ /combo
"""
    await update.message.reply_text(mensagem)

# ---------------- RESULTADO ----------------
async def resultado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """🎯 RESULTADO FINAL – ANÁLISE

✅ Flamengo vence
✅ Palmeiras ou empate (1X)
✅ Real Madrid vence
✅ Juventus ou empate (1X)
✅ Bayern vence

📊 Probabilidade: Média/Alta
"""
    await update.message.reply_text(mensagem)

# ---------------- OVER ----------------
async def over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """🔥 OVER / UNDER – GOLS

✅ Flamengo x Cruzeiro → Over 1.5
✅ Palmeiras x Santos → Over 2.5
✅ Real Madrid x Betis → Over 2.5
❌ Juventus x Milan → Under 2.5
✅ Bayern x Leverkusen → Over 2.5
"""
    await update.message.reply_text(mensagem)

# ---------------- ESCANTEIOS ----------------
async def escanteios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """🚩 ESCANTEIOS – ANÁLISE

✅ Flamengo x Cruzeiro → Over 8.5
✅ Palmeiras x Santos → Over 9.5
✅ Real Madrid x Betis → Over 9.5
✅ Bayern x Leverkusen → Over 10.5
"""
    await update.message.reply_text(mensagem)

# ---------------- COMBO ----------------
async def combo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """💎 COMBO DO DIA – ATLAS TIPS

✅ Flamengo vence
✅ Real Madrid vence
✅ Over 1.5 Bayern
✅ Over 8.5 Palmeiras

🎯 Odd média: 3.20
💰 Stake: R$10 a R$30
"""
    await update.message.reply_text(mensagem)

# ---------------- MAIN ----------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", jogos))
    app.add_handler(CommandHandler("resultado", resultado))
    app.add_handler(CommandHandler("over", over))
    app.add_handler(CommandHandler("escanteios", escanteios))
    app.add_handler(CommandHandler("combo", combo))

    print("🤖 Bot Atlas iniciado...")
    app.run_polling()

if _name_ == "_main_":
    main()
