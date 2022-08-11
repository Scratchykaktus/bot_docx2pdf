import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes

import os

from data import config
import markups as nav
import convert_class as convert

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


# Команда START
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    with open('files/img/converter.jpg', 'rb') as photo:
        await message.answer_photo(photo=photo,
                                   caption="Привет! Это тестовый бот T1verd, который "
                                           "может проеобразовать твои файлы в другие форматы!\n"
                                           "Для начала работы выбери формат своего файла",
                                   reply_markup=nav.main_menu())


# Команда HELP
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    with open('files/img/converter.jpg', 'rb') as photo:
        await message.answer_photo(photo=photo,
                                   caption="Данный бот позволяет конвертировать формат твоего файла "
                                           "в любой другой!\n"
                                           "Для этого необходимо сначала выберать тип своего файла, "
                                           "а затем выбрать в какой формат его преобразовать",
                                   reply_markup=nav.main_menu())


# При отправки неизвестной команды
@dp.message_handler()
async def cmd_unknown(message: types.Message):
    if message.text == 'Что умеет этот бот?':
        await cmd_help(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text='Что умеет этот бот?'))

        await message.answer(text='Извини, я не понимаю.. Для ознакомления с ботом, нажми кнопку ниже или напиши /help',
                             reply_markup=keyboard)


# Обработчик callback
@dp.callback_query_handler(nav.format_cb.filter(action=['doc', 'img', 'audio', 'video', 'back']))
async def cmd_doc(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]
    if action == 'doc':
        with open('files/img/word-to-pdf.png', 'rb') as photo:
            await call.message.edit_media(
                types.InputMediaPhoto(photo, caption='Выбирите в какой формат конвертировать:'),
                reply_markup=nav.update_form_doc())

    # elif action == 'img':
    #     with open('files/img/jpg-to-png.png', 'rb') as photo:
    #         await call.message.edit_media(
    #             types.InputMediaPhoto(photo, caption='Выбирите в какой формат конвертировать:'),
    #             reply_markup=nav.update_form_img())
    #
    # elif action == 'audio':
    #     await call.message.edit_caption('Выбирите в какой формат конвертировать:', reply_markup=nav.update_form_audio())
    #
    # elif action == 'video':
    #     await call.message.edit_caption('Выбирите в какой формат конвертировать:', reply_markup=nav.update_form_video())

    elif action == 'back':
        with open('files/img/converter.jpg', 'rb') as photo:
            await call.message.edit_media(types.InputMediaPhoto(photo,
                                                                caption="Данный бот позволяет конвертировать формат "
                                                                        "твоего файла в любой другой!\n"
                                                                        "Для этого необходимо сначала выберать тип "
                                                                        "своего файла, а затем выбрать в какой формат "
                                                                        "его преобразовать"),
                                          reply_markup=nav.main_menu())

    await call.answer()


# Очистка каталогов от скаченных и преобразованных файлов
def remove_dir(filename):
    os.remove(f'files/convert_files/{filename}.docx')
    # shutil.rmtree('files/convert_files/documents')
    os.remove(f'files/convert_files/success/{filename}.pdf')


@dp.callback_query_handler(nav.format_cb.filter(action=['pdf']))
async def cv_docx_pdf(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]
    if action == 'pdf':
        await call.answer('Отправьте docx файл для конвертирования', cache_time=2)
        # await call.message.answer('Ожидание файла...')
    await call.answer()


# При отправке документа
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def doc_handler(message: types.Message):
    # await message.answer('Загрузка файла')

    # file_id = message.document.file_id
    fname = message.document.file_name  # Полное имя файла

    # file = await bot.get_file(file_id)

    filename, file_expansion = os.path.splitext(fname)  # Сплитаем имя файла без типа

    # file_path = file.file_path

    destination = f'files/convert_files/{fname}'
    await message.document.download(destination_file=destination)
    # await message.answer('Скаченно')

    try:
        with open(convert.conv(fname), 'rb') as pdf:
            await message.answer_document(pdf)

    except NameError:
        await message.answer('Извините, бот может конвертировать документы только формата <b>docx</b>')

    finally:
        remove_dir(filename)

    # media = types.MediaGroup()
    # media.attach_document(types.InputFile)


def main():
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
