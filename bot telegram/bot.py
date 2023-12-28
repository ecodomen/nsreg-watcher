import requests
import telebot

# Инициализируйте бота Telegram
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")

# Функция проверки состояния обновления сервера
def check_server_upgrade_status():
    # Make a request to ecodomen.ru API to get the server upgrade status
    response = requests.get("https://ecodomen.ru/api/server_upgrade_status")
    if response.status_code == 200:
        return response.json()["status"]
    else:
        return "Failed to retrieve server upgrade status"

# Функция проверки неисправности компонентов системы
def check_system_components_failure():
    # Make a request to ecodomen.ru API to get the system components status
    response = requests.get("https://ecodomen.ru/api/system_components_status")
    if response.status_code == 200:
        components = response.json()["components"]
        failed_components = [component for component in components if not component["status"]]
        if failed_components:
            return [component["name"] for component in failed_components]
        else:
            return "No system components failure"
    else:
        return "Failed to retrieve system components status"

# Функция для проверки ошибок парсера
def check_parser_failures():
    # Make a request to ecodomen.ru API to get the parser failures status
    response = requests.get("https://ecodomen.ru/api/parser_failures_status")
    if response.status_code == 200:
        failures = response.json()["failures"]
        if failures:
            return [failure["name"] for failure in failures]
        else:
            return "No parser failures"
    else:
        return "Failed to retrieve parser failures status"

# Обработка команды /status
@bot.message_handler(commands=['status'])
def handle_status_command(message):
    server_upgrade_status = check_server_upgrade_status()
    system_components_failure = check_system_components_failure()
    parser_failures = check_parser_failures()

    response = f"Server Upgrade Status: {server_upgrade_status}\n\n"
    response += "System Components Failure:\n"
    if isinstance(system_components_failure, list):
        response += "\n".join(system_components_failure)
    else:
        response += system_components_failure
    response += "\n\n"

    response += "Parser Failures:\n"
    if isinstance(parser_failures, list):
        response += "\n".join(parser_failures)
    else:
        response += parser_failures

    bot.reply_to(message, response)

# Запустите бота
bot.polling()