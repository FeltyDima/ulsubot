from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from src.keyboards.keyboards import *
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import sqlite3
from googletrans import Translator

translator = Translator()
router: Router = Router()
DATABASE = 'homewor.db'


def create_connection():
    """Создает соединение с базой данных"""
    return sqlite3.connect('users.db')


def create_user_if_not_exists(user_id):
    """Создает пользователя, если его нет в базе данных, и устанавливает английский язык по умолчанию"""
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, language TEXT)')
        cursor.execute(
            'INSERT OR IGNORE INTO users (user_id, language) VALUES (?, ?)', (user_id, 'en'))
        conn.commit()


def get_user_language(user_id):
    """Возвращает язык пользователя"""
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT language FROM users WHERE user_id = ?', (user_id,))
        language = cursor.fetchone()
        return language[0] if language else None


def set_user_language(user_id, language):
    """Устанавливает язык пользователя"""
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'REPLACE INTO users (user_id, language) VALUES (?, ?)', (user_id, language))
        conn.commit()


async def translate_message(lang: str, text: str) -> str:
    """Функция для перевода сообщения на нужный язык"""
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"


def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS homewor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


class HomeworkStates(StatesGroup):
    name = State()
    homework = State()
    date = State()
    number_delete = State()


@router.message(Command("start"))
async def process_any_message(message: Message):
    create_user_if_not_exists(message.from_user.id)
    user_language = get_user_language(message.from_user.id)
    text = "Hello! How can I help you?"
    response = await translate_message(user_language, text)
    await message.answer(response, reply_markup=start_kb())


@router.message(F.text == "Diary")
async def answer_yes(message: Message):
    user_language = get_user_language(message.from_user.id)
    text = 'In this section you can store your homework'
    response = await translate_message(user_language, text)
    await message.answer(
        response, reply_markup=homework_kb()
    )


@router.message(F.text == "Write homework")
async def write_homework(message: Message, state: FSMContext):
    user_language = get_user_language(message.from_user.id)
    text = 'Enter the subject:'
    response = await translate_message(user_language, text)
    await message.answer(
        response, reply_markup=ReplyKeyboardRemove())
    await state.set_state(HomeworkStates.name)


@router.message(HomeworkStates.name)
async def fgdgfd(message: Message, state: FSMContext):
    await state.update_data(name_homework=message.text.lower())
    user_language = get_user_language(message.from_user.id)
    text = 'Enter a description:'
    response = await translate_message(user_language, text)
    await message.answer(
        response
    )
    await state.set_state(HomeworkStates.homework)


@router.message(HomeworkStates.homework)
async def fgdgdrfgfd(message: Message, state: FSMContext):
    await state.update_data(homeworks=message.text.lower())
    user_language = get_user_language(message.from_user.id)
    text = 'Enter the delivery date(YYYY-MM-DD):'
    response = await translate_message(user_language, text)
    await message.answer(
        response
    )
    await state.set_state(HomeworkStates.date)


@router.message(HomeworkStates.date)
async def sadfiudasuifh(message: Message, state: FSMContext):
    user_data = await state.get_data()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
            INSERT INTO homewor (user_id, subject, description, due_date)
            VALUES (?, ?, ?, ?)
        ''', (message.from_user.id, user_data['name_homework'], user_data['homeworks'], message.text.lower()))
    conn.commit()
    conn.close()

    await state.clear()
    user_language = get_user_language(message.from_user.id)
    text = 'The homework has been added successfully!'
    response = await translate_message(user_language, text)
    await message.answer(response, reply_markup=homework_kb())


@router.message(F.text == "Read homework")
async def view_homework(message: Message):
    user_id = message.from_user.id
    print(user_id)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        'SELECT subject, description, due_date FROM homewor WHERE user_id=?', (user_id,))
    rows = c.fetchall()
    conn.close()

    user_language = get_user_language(message.from_user.id)
    text1 = 'No homework was found.'
    response1 = await translate_message(user_language, text1)
    text2 = 'Subject'
    response2 = await translate_message(user_language, text2)
    text3 = 'Description'
    response3 = await translate_message(user_language, text3)
    text4 = 'Date of delivery'
    response4 = await translate_message(user_language, text4)

    if not rows:
        await message.answer(response1)
    else:
        response = ""
        a = 0
        for row in rows:
            a += 1
            response += f"{a}){response2} {row[0]}\n{response3} {row[1]}\n{response4} {row[2]}\n\n"
        await message.answer(response, parse_mode="Markdown", reply_markup=delete_kb())


@router.message(F.text == "Delete one")
async def delete_homework(message: types.Message, state: State):
    user_language = get_user_language(message.from_user.id)
    text = 'Enter the number of the task you want to delete:'
    response = await translate_message(user_language, text)
    await message.reply(response)
    await state.set_state(HomeworkStates.number_delete)


@router.message(HomeworkStates.number_delete)
async def process_delete(message: types.Message, state: FSMContext):
    task_id = int(message.text)
    user_id = message.from_user.id

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM homewor WHERE user_id=? AND id=?',
              (user_id, task_id))
    conn.commit()
    conn.close()

    await state.clear()
    user_language = get_user_language(message.from_user.id)
    text = 'The homework has been successfully deleted!'
    response = await translate_message(user_language, text)
    await message.answer(response)


@router.message(F.text == 'Delete all')
async def delete_all_homework(message: types.Message):
    user_id = message.from_user.id

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM homewor WHERE user_id=?', (user_id,))
    conn.commit()
    conn.close()

    user_language = get_user_language(message.from_user.id)
    text = 'All homework has been successfully deleted!'
    response = await translate_message(user_language, text)
    await message.answer(response)


@router.message(F.text == "The main⬅️")
async def back(message: Message):
    await message.delete()
    user_language = get_user_language(message.from_user.id)
    text = 'Hi!!! Choose the functionality.'
    response = await translate_message(user_language, text)
    await message.answer(
        response, reply_markup=start_kb()
    )


@router.message(F.text == "Recreation")
async def back(message: Message):
    await message.delete()
    user_language = get_user_language(message.from_user.id)
    text = 'In this section you can get acquainted with the sights of UlSU'
    response = await translate_message(user_language, text)
    await message.answer(
        response, reply_markup=recreation_kb()
    )


@router.message(F.text == "Language")
async def back(message: Message):
    response = "Please choose a language / Пожалуйста, выберите язык"
    keyboard = create_language_keyboard()
    await message.answer(response, reply_markup=keyboard)


@router.message(F.text == "Russian")
async def write_homework(message: Message, state: FSMContext):
    set_user_language(message.from_user.id, 'ru')
    text = 'Язык изменен на русский. Выберите функционал: '
    await message.answer(
        text, reply_markup=start_kb())


@router.message(F.text == "English")
async def write_homework(message: Message, state: FSMContext):
    set_user_language(message.from_user.id, 'en')
    text = 'The language has been changed to English. Select functionality: '
    await message.answer(
        text, reply_markup=start_kb())


@router.callback_query(F.data == 'musem')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile('.\\src\\image\\photo_10_2024-06-03_16-50-06.jpg'), reply_markup=back_kb())


@router.callback_query(F.data == 'cinema')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile('.\\src\\image\\photo_4_2024-06-03_16-50-06.jpg'''), reply_markup=back_kb())


@router.callback_query(F.data == 'Amphitheater')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_7_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == '#ulgu')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_1_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == 'kworking')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_11_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == 'pin')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_8_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == 'tennis')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_6_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == 'photozone')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_9_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.callback_query(F.data == 'Bridge')
async def musem(clbck: CallbackQuery):
    await clbck.message.answer_photo(FSInputFile(".\\src\\image\\photo_3_2024-06-03_16-50-06.jpg"), reply_markup=back_kb())


@router.message(F.text == "Bots")
async def answer_yes(message: Message):
    user_language = get_user_language(message.from_user.id)
    text = 'List of important bots and links'
    response = await translate_message(user_language, text)
    await message.answer(
        text=f'''{response}
        \n[Portal ULSU](https://portal.ulsu.ru)
        \n[VK Group](https://vk.com/ulsu_ulgu)
        \n[Telegram Channel](https://t.me/inform_ulsu)
        \n[YouTube Channel](https://www.youtube.com/c/73pressulsu)
        \n[ULSU Timetable of classes](https://t.me/ulsurobot)''',
        disable_web_page_preview=True,
        reply_markup=back_kb(),
        parse_mode='Markdown'
    )


@router.message(F.text == "Departments")
async def answer_yes(message: Message):
    user_language = get_user_language(message.from_user.id)
    text = 'Select department:'
    response = await translate_message(user_language, text)
    await message.answer(response, reply_markup=departments_kb())


@router.message(lambda message: message.text in departments.keys())
async def show_teachers(message: types.Message):
    user_language = get_user_language(message.from_user.id)
    department = message.text
    head = departments[department]["head"]
    teachers = departments[department]["teachers"]
    text1 = await translate_message(user_language, 'Head of the department:')
    text2 = await translate_message(user_language, 'Teachers:')
    response = f"🗂 <b>{department}</b>\n\n"
    response += f"🔝 <b>{text1}</b>\n"
    response += f"👨‍🏫 <b>{head['name']}</b>\n"
    if head.get('description'):
        response += f"   {await translate_message(user_language, head['description'])}\n"
    response += f"\n<b>{text2}</b>\n"

    for i, teacher in enumerate(teachers, 1):
        response += f"👨‍🏫 {i}. <b>{teacher['name']}</b>\n"
        if teacher.get('description'):
            response += f"   {await translate_message(user_language, teacher['description'])}\n"

    await message.reply(response, parse_mode='HTML')


@router.message(F.text == "FAQ")
async def faq(message: Message):
    user_language = get_user_language(message.from_user.id)
    text = 'List of popular questions: '
    response = await translate_message(user_language, text)
    await message.answer(
        text=response,
        reply_markup=faq_kb(message.from_user.id)
    )


@router.callback_query(lambda c: c.data in faq_data.keys())
async def handle_faq_answer(callback_query: types.CallbackQuery, state: FSMContext):
    answer = faq_data[callback_query.data]
    user_language = get_user_language(callback_query.message.chat.id)
    response = await translate_message(user_language, answer)
    await callback_query.answer(response, show_alert=True)
