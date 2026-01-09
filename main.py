#!/usr/bin/env python3

from dotenv import load_dotenv
import os

# Для python-telegram-bot >= 20.0
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from pokerapp.config import Config
from pokerapp.pokerbot import PokerBot


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Texas Poker Bot запущен! Используйте /ready")


async def ready_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Вы готовы к игре!")


def main() -> None:
    load_dotenv()
    cfg: Config = Config()

    if cfg.TOKEN == "":
        print("Environment variable POKERBOT_TOKEN is not set")
        exit(1)

    # Для теста - запускаем простого бота
    print(f"🤖 Токен: {cfg.TOKEN[:10]}...")
    
    # Создаем Application (новая версия API)
    application = Application.builder().token(cfg.TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("ready", ready_command))
    
    print("✅ Бот запускается...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()