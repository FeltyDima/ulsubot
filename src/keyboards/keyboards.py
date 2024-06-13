from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

languages = {
    'en': 'English',
    'ru': 'Russian'
}


def create_language_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру с кнопками для выбора языка"""
    # Предполагаем, что languages - это словарь с названиями языков
    buttons = [KeyboardButton(text=lang_name)
               for lang_name in languages.values()]
    # Создаем объект клавиатуры и передаем список кнопок в конструктор
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
    return keyboard


def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Diary")
    kb.button(text="Recreation")
    kb.button(text="Bots")
    kb.button(text="Language")
    kb.button(text="Departments")
    kb.button(text="FAQ")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)


def back_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="The main⬅️")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def homework_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Write homework")
    kb.button(text="Read homework")
    kb.button(text="The main⬅️")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def delete_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Delete one")
    kb.button(text="Delete all")
    kb.button(text="The main⬅️")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def back_to_main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='The main⬅️', callback_data='back')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_language_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🇺🇸 English", callback_data='lang_en'),
         InlineKeyboardButton(text="🇷🇺 Русский", callback_data='lang_ru')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


departments = {
    "Кафедра прикладной математики": {
        "head": {
            "name": "Бутов Александр Александрович",
            "description": "Заведующий кафедрой"
        },
        "teachers": [
            {"name": "Самойлов Леонид Михайлович",
                "description": "Доктор физико-математических наук, профессор"},
            {"name": "Богданов Андрей Юрьевич",
                "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Бурмистрова Валентина Геннадьевна",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Веревкин Андрей Борисович",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Воденин Дмитрий Ростиславович",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Гаврилова Мария Сергеевна",
             "description": "Кандидат физико-математических наук, старший преподаватель"},
            {"name": "Савинов Юрий Геннадьевич",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Фролова Юлия Юрьевна",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Хрусталев Сергей Александрович",
             "description": "Кандидат физико-математических наук, доцент"}
        ]
    },
    "Кафедра информационных технологий": {
        "head": {
            "name": "Волков Максим Анатольевич",
            "description": "Декан, Заведующий кафедрой"
        },
        "teachers": [
            {"name": "Жаркова Галина Алексеевна",
                "description": "Доктор педагогических наук, профессор"},
            {"name": "Санкин Николай Юрьевич",
                "description": "Кандидат технических наук, доцент"},
            {"name": "Семушин Иннокентий Васильевич",
             "description": "Доктор технических наук, профессор"},
            {"name": "Угаров Владимир Васильевич",
                "description": "Кандидат технических наук, доцент"},
            {"name": "Филаткина Елена Владимировна",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Цыганова Юлия Владимировна",
                "description": "Доктор физико-математических наук, профессор"},
            {"name": "Чичев Александр Алексеевич",
             "description": "Старший преподаватель"}

        ]
    },
    "Кафедра математического моделирования технических систем": {
        "head": {
            "name": "Санников Игорь Алексеевич",
            "description": "Заведующий кафедрой, Доцент"
        },
        "teachers": [
            {"name": "Базаров Владимир Владимирович",
                "description": "Aссистент"},
            {"name": "Блюменштейн Алексей Александрович",
                "description": "Cтарший преподаватель"},
            {"name": "Евсеев Александр Николаевич",
                "description": "Кандидат технических наук, доцент"},
            {"name": "Егоров Кирилл Александрович",
             "description": "Aссистент"},
            {"name": "Егоров Павел Александрович",
                "description": "Aссистент"},
            {"name": "Еремин Александр Александрович",
             "description": "Доцент"},
            {"name": "Железнов Олег Владимирович",
                "description": "Кандидат технических наук, доцент"},
            {"name": "Калинов Евгений Дмитриевич",
             "description": "Старший преподаватель"},
            {"name": "Левкина Ольга Юрьевна",
                "description": "Кандидат технических наук, доцент"},
            {"name": "Кондратьева Анна Сергеевна",
             "description": "Старший преподаватель"},
            {"name": "Мешихин Александр Александрович",
                "description": "Старший преподаватель"},
            {"name": "Моисеев Константин Юрьевич",
             "description": "Доцент"},
            {"name": "Павлов Павел Юрьевич",
                "description": "Старший преподаватель"},
            {"name": "Полянсков Юрий Вячеславович",
             "description": "Президент УлГУ, профессор"},
            {"name": "Рыжаков Станислав Геннадьевич",
                "description": "Профессор"},
            {"name": "Санников Игорь Алексеевич",
             "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Сидорова Алена Игоревна",
                "description": "Старший преподаватель"},
            {"name": "Торбин Сергей Викторович",
             "description": "Старший преподаватель"},
            {"name": "Шабалкин Дмитрий Юрьевич",
                "description": "Кандидат физико-математических наук, доцент"},
            {"name": "Щуров Илья Владимирович",
             "description": "Старший преподаватель"},
            {"name": "Ярдаева Маргарита Николаевна",
             "description": "Старший преподаватель"},

        ]
    },
    "Кафедра информационной безопасности и теории управления": {
        "head": {
            "name": "Андреев Александр Сергеевич",
            "description": "Профессор, Заведующий кафедрой"
        },
        "teachers": [
            {"name": "Рацеев Сергей Михайлович",
                "description": ""},
            {"name": "Иванцов Андрей Михайлович",
                "description": ""},
            {"name": "Юрьева Ольга Дмитриевна",
                "description": ""},
            {"name": "Перцева Ирина Анатольевна",
                "description": ""},
            {"name": "Сутыркина Екатерина Алексеевна",
                "description": ""},
            {"name": "Петровичева Юлия Владимировна",
                "description": ""}
        ]
    },
    "Кафедра телекоммуникационных технологий и сетей": {
        "head": {
            "name": "Смагин Алексей Аркадьевич",
            "description": "Профессор, Заведующий кафедрой"
        },
        "teachers": [
            {"name": "Смолеха Виталий Петрович",
                "description": ""},
            {"name": "Чекал Елена Георгиевна",
                "description": ""},
            {"name": "Козловский Вячеслав Геннадьевич",
                "description": ""},
            {"name": "Липатова Светлана Валерьевна",
                "description": ""},
            {"name": "Курилова Оксана Леонидовна",
                "description": ""},
            {"name": "Булаев Алексей Александрович",
                "description": ""},
            {"name": "Бочкарева Юлия Евгеньевна",
                "description": ""}
        ]
    },
    "Кафедра цифровых технологий авиационного производства": {
        "head": {
            "name": "Еремин Александр Александрович",
            "description": "Заведующий кафедрой, Доцент"
        },
        "teachers": [
            {"name": "——"}
        ]
    },
    "Кафедра информационных технологий и защиты информации": {
        "head": {
            "name": "Кукин Евгений Серафимович",
            "description": "Заведующий кафедрой"
        },
        "teachers": [
            {"name": "——"}
        ]
    },
}


def departments_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for department in departments.keys():
        keyboard.button(text=f"{department}")
    keyboard.button(text="The main⬅️")
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True)


# Список вопросов и ответов
faq_data = {
    "1": "В библиотеке университета можно отдохнуть на мягких кубиках, также там можно делать свои дела по учебе на специальных столиках для учебы, так же в фойе первого корпуса есть удобные пуфики.",
    "2": "В нашем университете есть 2 столовые с разными вкусными блюдами! Так же имеется кафе экватор с большим разнообразием еды.",
    "3": "В университете, рядом с библиотекой, есть кабинет, где вам распечатают всё, что вам нужно",
    "4": "Учебная - за хорошую успеваемость, научно-исследовательская - за вклад в научную деятельность университета, спортивная - за спортивные достижения и тд.",
    "5": "На каждом факультете имеется студенческий актив где вы можете прокачивать свои софт скиллы и просто классно проводить время! Так же в УлГУ имеется музей где вы можете узнать историю университета",
    "6": "За улкойны, получаемые за достижения в активе, вы можете купить мерч университета, поездку в другой город и тд.",
    "7": "Первые три корпуса удобно соединены между собой специальными переходами, но чтобы прийти в 4 и 5 корпус все равно придется выйти на улицу, к счастью эти корпуса не основные!",
    "8": "На территории нашего университета можно курить в специально отведенных местах, которые расположены возле входов в корпуса"
}


def recreation_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Музей УЛГУ',
                              callback_data='musem'),
         InlineKeyboardButton(text='Летний кинотетр',
                              callback_data='cinema')],
        [InlineKeyboardButton(text='Амфитеатр',
                              callback_data='Amphitheater'),
         InlineKeyboardButton(text='#УЛГУ',
                              callback_data='#ulgu')],
        [InlineKeyboardButton(text='Kworking',
                              callback_data='kworking'),
         InlineKeyboardButton(text='Пин-арт',
                              callback_data='pin')],
        [InlineKeyboardButton(text='Тениссные корты',
                              callback_data='tennis'),
         InlineKeyboardButton(text='Фотозона',
                              callback_data='photozone')],
        [InlineKeyboardButton(text='Мост "Дружбы"',
                              callback_data='Bridge')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def faq_kb(id):
    button = [
        [InlineKeyboardButton(
            text="Где можно отдохнуть в свободное от занятий время?", callback_data='1')],
        [InlineKeyboardButton(
            text="Что делать, если я проголодался/ась в университете?", callback_data='2')],
        [InlineKeyboardButton(
            text="Что делать если у меня нет принтера?", callback_data='3')],
        [InlineKeyboardButton(
            text="Какие виды стипендии бывают?", callback_data='4')],
        [InlineKeyboardButton(
            text="Чем можно заняться в университете в свободное время?", callback_data='5')],
        [InlineKeyboardButton(
            text="Что я получу за достижения в студенческом активе?", callback_data='6')],
        [InlineKeyboardButton(
            text="Как перейти в другой корпус, не выходя на улицу?", callback_data='7')],
        [InlineKeyboardButton(
            text="Можно ли курить на территории улгу?", callback_data='8')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
