import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Option 1")],
        [KeyboardButton("Option 2")],
        [KeyboardButton("Option 3")],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="به بات پیشبینز خوش آمدید",
        reply_markup=reply_markup,
        parse_mode="MarkdownV2",
    )


def main() -> None:
    application = (
        ApplicationBuilder()
        .token("6439138310:AAFJgQi2O7fSGmaTLo3LOQl9oeY75NOwaXk")
        .build()
    )

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
