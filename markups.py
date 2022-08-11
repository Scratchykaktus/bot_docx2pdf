from aiogram import types
from aiogram.utils.callback_data import CallbackData

format_cb = CallbackData('foramt', 'action')

#---- Главное меню ----
def main_menu():
    bt_doc = types.InlineKeyboardButton(text='documents', callback_data=format_cb.new(action='doc'))
    # bt_img = types.InlineKeyboardButton(text='images', callback_data=format_cb.new(action='img'))
    # bt_audio = types.InlineKeyboardButton(text='audio', callback_data=format_cb.new(action='audio'))
    # bt_video = types.InlineKeyboardButton(text='video', callback_data=format_cb.new(action='video'))

    keyboard = types.InlineKeyboardMarkup().add(bt_doc)
    # keyboard.row(bt_doc, bt_img)
    # keyboard.row(bt_audio, bt_video)

    return keyboard


#---- Меню для документов ----
def update_form_doc():
    formats = [
        types.InlineKeyboardButton(text='PDF', callback_data=format_cb.new(action='pdf')),
        types.InlineKeyboardButton(text='DOCX', callback_data=format_cb.new(action='doc'))
    ]
    bt_back = types.InlineKeyboardButton(text='<< Вернуться к выбору типа файла', callback_data=format_cb.new(action='back'))
    
    keyboard = types.InlineKeyboardMarkup(row_width=3)

    keyboard.add(*formats)
    keyboard.row(bt_back)

    return keyboard

#---- Форма с конпками для изображений----
# def update_form_img():
#     formats = [
#         types.InlineKeyboardButton(text='JPEG', callback_data=format_cb.new(action='1')),
#         types.InlineKeyboardButton(text='RAW', callback_data=format_cb.new(action='2')),
#         types.InlineKeyboardButton(text='PNG', callback_data=format_cb.new(action='3')),
#         types.InlineKeyboardButton(text='GIF', callback_data=format_cb.new(action='4')),
#         types.InlineKeyboardButton(text='BMP', callback_data=format_cb.new(action='5'))
#     ]
#     bt_back = types.InlineKeyboardButton(text='<< Вернуться к выбору типа файла', callback_data=format_cb.new(action='back'))
    
#     keyboard = types.InlineKeyboardMarkup(row_width=3)

#     keyboard.add(*formats)
#     keyboard.row(bt_back)

#     return keyboard

#---- Форма с конпками для аудио----
# def update_form_audio():
#     formats = [
#         types.InlineKeyboardButton(text='WAV', callback_data=format_cb.new(action='1')),
#         types.InlineKeyboardButton(text='MP3', callback_data=format_cb.new(action='2')),
#         types.InlineKeyboardButton(text='CVS', callback_data=format_cb.new(action='3')),
#         types.InlineKeyboardButton(text='IMA', callback_data=format_cb.new(action='4')),
#         types.InlineKeyboardButton(text='M4A', callback_data=format_cb.new(action='5')),
#         types.InlineKeyboardButton(text='M4R', callback_data=format_cb.new(action='6')),
#         types.InlineKeyboardButton(text='OGG', callback_data=format_cb.new(action='7'))
#     ]
#     bt_back = types.InlineKeyboardButton(text='<< Вернуться к выбору типа файла', callback_data=format_cb.new(action='back'))
    
#     keyboard = types.InlineKeyboardMarkup(row_width=3)

#     keyboard.add(*formats)
#     keyboard.row(bt_back)

#     return keyboard

#---- Форма с конпками для видео----
# def update_form_video():
#     formats = [
#         types.InlineKeyboardButton(text='MP4', callback_data=format_cb.new(action='1')),
#         types.InlineKeyboardButton(text='MOV', callback_data=format_cb.new(action='2')),
#         types.InlineKeyboardButton(text='MPEG', callback_data=format_cb.new(action='3')),
#         types.InlineKeyboardButton(text='MPEG-2', callback_data=format_cb.new(action='4')),
#         types.InlineKeyboardButton(text='WMV', callback_data=format_cb.new(action='5')),
#         types.InlineKeyboardButton(text='AVI', callback_data=format_cb.new(action='6')),
#         types.InlineKeyboardButton(text='WEBM', callback_data=format_cb.new(action='7')),
#         types.InlineKeyboardButton(text='SWF', callback_data=format_cb.new(action='8'))
#     ]
#     bt_back = types.InlineKeyboardButton(text='<< Вернуться к выбору типа файла', callback_data=format_cb.new(action='back'))
    
#     keyboard = types.InlineKeyboardMarkup(row_width=3)

#     keyboard.add(*formats)
#     keyboard.row(bt_back)

#     return keyboard
