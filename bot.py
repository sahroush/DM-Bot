from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store registered users
registered_users = {}

# Define the start command
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in registered_users:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Use /help to see available commands.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome back!")

# Define the help command
def help_command(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Available commands:\n/start - Display a welcome message\n/help - Show help\n/register - Register with a 9-digit number")

# Define the register command
def register(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id in registered_users:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are already registered.")
    else:
        args = context.args
        if len(args) == 1 and args[0].isdigit() and len(args[0]) == 9:
            number = args[0]
            if number in registered_users.values():
                context.bot.send_message(chat_id=update.effective_chat.id, text="This number is already connected to another user.")
            else:                
                registered_users[user_id] = number
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"Registration successful! Your number: {number}")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid format. Please use /register followed by a 9-digit number.")
# Main function to start the bot
def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("6439138310:AAFJgQi2O7fSGmaTLo3LOQl9oeY75NOwaXk")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("register", register, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
