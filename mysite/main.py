import telebot
from mysite.settings import TELEGRAM_BOT_TOKEN
import requests
# Создаем экземпляр бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

PICKUP_OR_DELIVERY = "1. Самовывоз\n2. Доставка"
PAYMENT_METHOD = "1. Наличными\n2. Картой"
    
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):

    # Отправляем приветственное сообщение и запрашиваем способ доставки
    bot.send_message(message.chat.id, "Здравствуйте! Выберите способ доставки:")
    bot.send_message(message.chat.id, PICKUP_OR_DELIVERY)
    # res = requests.get(url="http://127.0.0.1:8000/brand/?name=string")
    # # res.encoding()
    # dict_res = res.json()
    # bot.send_message(message.chat.id, dict_res[0]["name"])


# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Проверяем, что пользователь выбрал
    if message.text == "1":
        # Пользователь выбрал самовывоз
        bot.send_message(message.chat.id, "Вы выбрали самовывоз.\nНаш адрес ....")
        bot.register_next_step_handler(message, get_payment_method)

    elif message.text == "2":
        # Пользователь выбрал доставку
        bot.send_message(message.chat.id, "Вы выбрали доставку.")
        # Запрашиваем адрес и номер телефона
        bot.send_message(message.chat.id, "Введите ваш адрес:")
        bot.register_next_step_handler(message, get_address)
    else:
        # Пользователь ввел что-то другое
        bot.send_message(message.chat.id, "Некорректный ввод. Пожалуйста, выберите способ доставки.")

# Обработчик адреса
def get_address(message):
    # Сохраняем адрес
    address = message.text
    # Запрашиваем номер телефона
    bot.send_message(message.chat.id, "Введите ваш номер телефона:")
    bot.register_next_step_handler(message, get_phone_number)

# Обработчик номера телефона
def get_phone_number(message):
    # Сохраняем номер телефона
    phone_number = message.text
    # Сохраняем данные в базу данных
    # ...

    # Отправляем подтверждение
    bot.send_message(message.chat.id, "Спасибо! Ваши данные сохранены.")
    bot.register_next_step_handler(message, get_payment_method)


# Обработчик выбора способа оплаты
def get_payment_method(message):
    # Запрашиваем способ оплаты
    bot.send_message(message.chat.id, "Выберите способ оплаты:")
    bot.send_message(message.chat.id, "1. Наличными\n2. Картой")
    bot.register_next_step_handler(message, get_payment_details)

# Обработчик ввода данных оплаты
def get_payment_details(message):
    # Проверяем, что пользователь выбрал
    if message.text == "1":
        # Пользователь выбрал оплату наличными
        bot.send_message(message.chat.id, "Вы выбрали оплату наличными.")
    elif message.text == "2":
        # Пользователь выбрал оплату картой
        bot.send_message(message.chat.id, "Вы выбрали оплату картой.")
        # Запрашиваем данные карты
        bot.send_message(message.chat.id, "Введите номер карты:")
        bot.register_next_step_handler(message, get_card_number)
    else:
        # Пользователь ввел что-то другое
        bot.send_message(message.chat.id, "Некорректный ввод. Пожалуйста, выберите способ оплаты.")

# Обработчик номера карты
def get_card_number(message):
    # Сохраняем номер карты
    card_number = message.text
    # Запрашиваем срок действия карты
    bot.send_message(message.chat.id, "Введите срок действия карты (MM/YY):")
    bot.register_next_step_handler(message, get_card_expiration)

# Обработчик срока действия карты
def get_card_expiration(message):
    # Сохраняем срок действия карты
    card_expiration = message.text
    # Запрашиваем CVV-код
    bot.send_message(message.chat.id, "Введите CVV-код:")
    bot.register_next_step_handler(message, get_card_cvv)

# Обработчик CVV-кода
def get_card_cvv(message):
    # Сохраняем CVV-код
    card_cvv = message.text
    # Сохраняем данные в базу данных
    # ...

    # Отправляем подтверждение
    bot.send_message(message.chat.id, "Спасибо! Ваши данные сохранены.")

# Запускаем бота
bot.polling()
