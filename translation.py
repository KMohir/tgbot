translations={

    'ru':{
        "Tilni o'zgartirish":"Смена языка",
        'Tilni tanlang':'Выберите язык',
        'Tilni tanladingiz':'выбрали язык',
        'Salom,':'Здравствуйте,',
        'Operator bilan qanday aloqa qilishni tanlang':'Выберите способ связи с оператором',
        'Savolni yuboring...':'Отправьте вопрос...',
        'Texnik yordamga xabar yozish':'Написание сообщения в службу технической поддержки',
        'Texnik yordam bilan suhbatlashish':'Разговор с техподдержкой',
        "Juda ko'p so'rovlar!":'Слишком много запросов!',
        "Savol xato berildi operator bilan bog'lanish uchun pastki tugmani bosing":"Вопрос задан неправильно нажмите нижнюю кнопку, чтобы связаться с оператором",
        "Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing":"Хотите связаться со службой технической поддержки? Нажмите кнопку ниже",
        "Javob yozish uchun shu tugmani bosing":"Нажмите эту кнопку, чтобы написать ответ",
        "Sessiyani yakunlash":"Завершение сеанса",
        "Texnik yordamga ga xabar yozing":"Напишите сообщение в службу технической поддержки",
        "Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing!":"Хотите связаться со службой технической поддержки? Нажмите кнопку ниже!",
        "Qaysi proyekt da savolingiz bor":"В каком проекте у вас есть вопрос",
        "Siz bermoqchi  bo'lgan savolingizni yuboring":"Отправьте вопрос, который хотите задать",
        "Javobni kuting!":"Ждите ответа!",
        "Savolni text shaklida yuboring...":"Отправьте вопрос в текстовой форме...",
        "Javob sizni qoniqtirdimi":"Вас удовлетворил ответ",
        "Pastki tugmani bosip Savolni to'liq yozing nomerinigiz bilan!":"Введите полный вопрос, нажав нижнюю кнопку с вашим номером!",
        "Pastki tugmani bosip Savolni to'liq yozing har qanday shaklda audio , rasm , video. Nomerinigiz bilan!":"Напишите полный вопрос , нажав на нижнюю кнопку аудио , фото, видео в любом виде. С вашим номером!",
        "Sizga xat! Quyidagi tugmani bpyosish orqali javob berishingiz mumkin":"Письмо тебе! Вы можете ответить, нажав кнопку ниже",
        "Ha":"Да",
        "Yo'q":"Нет",
        'Xizmatimizdan foydalananangiz uchun rahmat\n/start - Savolni yuborish uchun,/help - Biz haqimizda':'Спасибо за использование нашего сервиса\n/start - отправить вопрос, /help - о нас',
        'Yuqoridagi tugmalardan birini tanlang':'Выберите одну из кнопок вверху',
        'Raqamingizni yuborish uchun pastdagi tugmani bosing':'Нажмите кнопку ниже, чтобы отправить свой номер',
        'Tugmani bosing':'Нажмите кнопку',
        "Siz yubormoqchi bo'lgan savolingizni to'liq shaklda yuboring":"Отправьте вопрос, который вы хотите отправить, в полной форме",
        "Operator bilan /ask ni bosip boglansez boladi":"Operator bilan /ask ni bosip boglansez boladi",
        "sizni savolingiz bizning operatorlarga yuborildi yaqin orada sizga javob beramiz":"ваш вопрос был отправлен нашим операторам мы ответим вам в ближайшее время",
        "Pastdagi tugmani bosing tugmani bosing":"Нажмите кнопку внизу Нажмите кнопку",
        "Ro'yxatdan o'tdingiz":"Вы прошли регистрацию ",
        "Rahmat savolimga javob oldim":"Спасибо, что получили ответ на мой вопрос",
    }

}

def _(text,lang='uz'):
    if lang=='uz':
        return text
    else:
        try:
            return translations[lang][text]
        except:
            return text