import telebot
from telebot import types

import order

bot = telebot.TeleBot('8003570121:AAES2C5VKLIdZrGG9JQz4e8tSOO3sfJ_if0')

botgt = telebot.TeleBot(bot)
chatid = '5871008116'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
    photo_instruction_SivchSP = open(r"D:\Captures\photos\SivchSP.jpg", 'rb')
    mess = f'------👋*Привет {message.from_user.first_name}!*------  \n \n👾_Очень рады тебя приветствовать в SivchSP!_\n \n 💰*Здесь вы можете приобрести в-баксы подарком по самым низким ценам!*'
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Магазин🛍', callback_data='buy_vbucks'))
    markup.add(types.InlineKeyboardButton('FAQ⁉', callback_data='FAQ'))

    bot.send_photo(message.from_user.id, photo=photo_instruction_SivchSP, caption=mess, reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda message: True)
def get_user_message(message):
    markup = types.InlineKeyboardMarkup()
    user_id = message.from_user.id
    user_name = message.from_user.username
    if (message.data == 'FAQ'):
        markup.add(types.InlineKeyboardButton('Часто задаваемые вопросы', url="https://telegra.ph/CHasto-zadavaemye-voprosy-11-22-5",parse_mode='Markdown'))
        bot.send_message(message.message.chat.id,"ℹ️*Перед обращением в поддержку обязательно посмотрите часто задаваемые вопросы*", reply_markup=markup, parse_mode='Markdown')

    if message.data == 'buy_vbucks':
        pedik = " \n \n------⚠️*В-БАКСЫ ПОДАРКОМ*⚠️------\n \n❗Перед покупкой обязательно добавьте актуальные подарочные ники в друзья.\nВсе ники в описании бота."
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('💸Выбрать количество в-баксов💸 ️', callback_data='quantity_vbucks'))
        markup.add(types.InlineKeyboardButton('💰Купить В-Баксы на аккаунт💰 ️', callback_data='vbucks_on_akk'))
        markup.add(types.InlineKeyboardButton('💬Отзывы', url="https://t.me/otz_sivchsp"))
        photo1 = open(r"D:\Captures\photos\fortnite.jpg", 'rb')
        markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
        bot.send_photo(message.from_user.id, photo=photo1, caption=pedik, reply_markup=markup, parse_mode='Markdown')
    if (message.data == 'quantity_vbucks'):
        mess2 = '💸Выберите нужное вам количество в-баксов💸 \n \n ❤Миннимум - 200 \n 💚Максимум - 5000 '
        markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
        bot.send_message(message.message.chat.id, mess2, reply_markup=markup)

    if (message.data == 'read'):
        photo_instruction = open(r"D:\Captures\photos\photo_buisnes.jpg", 'rb')
        markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
        bot.send_photo(message.from_user.id, photo=photo_instruction,
                       caption='📸Теперь нужно отправить сюда *СКРИНШОТ ЧЕКА / КВИТАНЦИИ* об оплате для подтверждения перевода.\n\n📝В подписи укажите: \n--Ваш ник в Эпик геймс \n--Предмет из магазина, который\n  вы выбрали за оплаченное \n  кол-во в-баксов.\n\n 🗂Файлом отправлять не нужно!',
                       reply_markup=markup,parse_mode='Markdown')
        bot.delete_message(message.message.chat.id, message.message.message_id - 2)
    if (message.data == 'payment'):
        markup = types.InlineKeyboardMarkup()
        alone = '\n🔵ОЗОН: ' + f'<code>{2204320370220677}</code>' + '\n \n📩 Получатель: Всеволод М.\n📝 В комментариях при переводе ничего не писать, не указывать.'
        markup.add(types.InlineKeyboardButton('Я оплатил ️', callback_data='read'))
        markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
        bot.send_message(message.message.chat.id, alone, reply_markup=markup , parse_mode='HTML')

    if (message.data == 'vbucks_on_akk'):
        markup = types.InlineKeyboardMarkup()
        alone2 = '-----------*ПРАЙС*-----------\n\n💰30000 VB - 6000₽💰'
        markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
        markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
        bot.send_message(message.message.chat.id, alone2, reply_markup=markup, parse_mode='Markdown')
    if (message.data == 'back'):
        bot.delete_message(message.message.chat.id, message.message.message_id )
@bot.message_handler()
def funcion(message):
    try:
        text = message.text
        float(text)
        if float(text) < 200:
            markup = types.InlineKeyboardMarkup()
            bot.send_message(message.chat.id,'Простите, похоже вы неверное количество в-баксов \n выберите от 200 до 5000 В-Баксов',reply_markup=markup)
        if float(text) == 200:
            buy = float(text) / 5.45
            markup = types.InlineKeyboardMarkup()
            res = '💰' + text + ' в-баксов будут стоить - ' + str(int(buy + 35)) + ' ₽' + '💰'
            markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
            markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
            bot.send_message(message.chat.id, res, reply_markup=markup)
        elif float(text) <= 500:
            buy = float(text) / 5.45
            markup = types.InlineKeyboardMarkup()
            res = '💰' + text + ' в-баксов будут стоить - ' + str(int(buy + 59)) + ' ₽' + '💰'
            markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
            markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
            bot.send_message(message.chat.id, res, reply_markup=markup)
        elif float(text) <= 1000:
            buy = float(text) / 5.45
            markup = types.InlineKeyboardMarkup()
            res = '💰' + text + ' в-баксов будут стоить - ' + str(int(buy + 60)) + ' ₽' + '💰'
            markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
            markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
            bot.send_message(message.chat.id, res, reply_markup=markup)
        elif 1000 < float(text) <= 1500:
            buy = float(text) / 5.45
            markup = types.InlineKeyboardMarkup()
            res = '💰' + text + ' в-баксов будут стоить - ' + str(int(buy + 70)) + ' ₽' + '💰'
            markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
            markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
            bot.send_message(message.chat.id, res, reply_markup=markup)
        elif 1000 < float(text) < 30000:
            buy = float(text) / 5.45
            markup = types.InlineKeyboardMarkup()
            res = '💰' + text + ' в-баксов будут стоить - ' + str(int(buy + 150)) + ' ₽' + '💰'
            markup.add(types.InlineKeyboardButton('Перейти к оплате ️', callback_data='payment'))
            markup.add(types.InlineKeyboardButton('Назад ️', callback_data='back'))
            bot.send_message(message.chat.id, res, reply_markup=markup)
        if float(text) > 5000:
            markup = types.InlineKeyboardMarkup()
            bot.send_message(message.chat.id,'_Простите, похоже вы неверное количество в-баксов \n выберите от 200 до 5000 В-Баксов_',reply_markup=markup,parse_mode='Markdown')
        if 9999999999 < float(text) < 19999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id, text="❌*Ваш запрос на заказ отклонён по причине 'Вы прислали не квитанцию'* - /start ",parse_mode='Markdown')
        if 19999999999 < float(text) < 29999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id, text="❌*Ваш запрос на заказ отклонён по причине 'Неверный предмет' вашего предмета нет в магазине или на сегодня все в-баксы купили😕* - /start ",parse_mode='Markdown')
        if 29999999999 < float(text) < 39999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id, text="❌*Ваш запрос на заказ отклонён по причине 'Вашего платежа нет в списках'* - /start ",parse_mode='Markdown')
        if 39999999999 < float(text) < 49999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id, text="❌*Ваш запрос на  заказ отклонён по причине 'Вы прислали не настоящую квитанцию'* - /start ",parse_mode='Markdown')
        if 49999999999 < float(text) < 59999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id,text='*😕Случилось недопонимание*😕\n\n_Пожалуйста проверьте чтобы все условия заказа соответствовали_',parse_mode='Markdown')
        if 59999999999 < float(text) < 69999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            bot.send_message(chat_id=get_user_id, text='✅_Ваш запрос на заказ принят администратором!_\n \n*В ближайшее время вас обслужим , ожидайте* ',parse_mode='Markdown')
        if 89999999999 < float(text) < 99999999999:
            get_user_id = message.text[-10] + message.text[-9] + message.text[-8] + message.text[-7] + message.text[-6] + message.text[-5] + message.text[-4] + message.text[-3] + message.text[-2] + message.text[-1]
            print(get_user_id)
            markup.add(types.InlineKeyboardButton('💬Оставить отзыв💬', url="https://t.me/otz_sivchsp"))
            bot.send_message(chat_id=get_user_id, text='-----------✅Заказ  сделан✅-----------\n \n🛍Уважаем(ый/ая)️' + ' @'+message.from_user.username + ', спешу вам сообщить о статусе вашего заказа! \n \n💬Будем очень рады вашему\nотзыву',reply_markup=markup )

    except:
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, '❌Я вас не понимаю❌',reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def calendar(message):
    markup = types.InlineKeyboardMarkup()
    photo = message.photo[-1].file_id
    bot.send_message(message.chat.id, '✅Ваш запрос успешно отправлен администратору\n на проверку. Постараемся как можно быстрее вас обслужить✅', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_photo(chat_id=chatid, photo=photo, caption=message.caption, parse_mode='html', reply_markup=markup)
    bot.send_message(chat_id=chatid, text='@' + message.from_user.username)
    bot.send_message(chat_id=chatid, text=message.from_user.id)
    bot.send_message(chat_id=chatid, text='❌1 - Не квитанция❌ \n❌2 - Неправильный предмет❌ \n❌3 - платежа нет❌ \n❌4 - фейк квитанция❌ \n♻5 - недопонимание♻\n✅6 - Принять✅\n✅9 - Заказ готов✅')



# message_username = bot.copy_message(chat_id=chatid, from_chat_id=message.message.chat.id, message_id=message.message.message_id -1)
# bot.send_message(chat_id=chatid,  text=message_username, reply_markup=markup)
# копирует и отправляет сообщение
bot.polling(none_stop=True)
