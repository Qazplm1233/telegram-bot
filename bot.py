import logging
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ТОКЕН БОТА - вставь сюда свой токен от @BotFather
TOKEN = "8356665343:AAFdYtbXeiMcZ5d4gtrYgzWJmOVa_voga4Q"

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Словарь замен
REPLACEMENTS = {
    "пенис": "riskingпенис",
    "крови": "krovi",
    "кровь": "llКровь",
    "хуй": "riskingХуй",
    "пизда": "riskingПизда",
    "расчленил": "llРасчленил",
    "Каннибал": "kannibal",
    "говно": "llГовно",
    "расчленение": "llРасчленениеll",
    "маньяк": "llМаньяк",
    "говнище": "llГовнище",
    "канибал": "kanibal",
    # Добавляй свои слова сюда
}

def censor_text(text: str) -> str:
    """Заменяет запрещённые слова"""
    new_text = text
    for bad_word, replacement in REPLACEMENTS.items():
        pattern = re.compile(r'\b' + re.escape(bad_word) + r'\b', re.IGNORECASE)
        new_text = pattern.sub(replacement, new_text)
    return new_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Отправь мне текст с «плохими» словами, "
        "а я заменю их так, чтобы Шедеврум пропустил запрос."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    original = update.message.text
    processed = censor_text(original)
    
    if processed == original:
        await update.message.reply_text("Текст не содержал запрещённых слов (по моему словарю).")
    else:
        await update.message.reply_text(f"Вот обработанный текст:\n\n{processed}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if name == "main":
    main()
