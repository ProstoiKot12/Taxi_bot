from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


select_language_button = [
    [InlineKeyboardButton(text='🇷🇺Русский', callback_data='select_language_russian')],
    [InlineKeyboardButton(text='🇹🇷Türkçe', callback_data='select_language_turkey')],
    [InlineKeyboardButton(text='🇺🇸English', callback_data='select_language_english')]
]

select_language_kb = InlineKeyboardMarkup(inline_keyboard=select_language_button)

transfer_about_button = [
    [InlineKeyboardButton(text='🔍Узнать про трансфер', callback_data='transfer_about_ru')]
]

transfer_about_ru_kb = InlineKeyboardMarkup(inline_keyboard=transfer_about_button)

pick_direction_button = [
    [InlineKeyboardButton(text='🗺️Выбрать направление', callback_data='pick_direction_ru')]
]

pick_direction_ru_kb = InlineKeyboardMarkup(inline_keyboard=pick_direction_button)

choice_inside_antalya_button = [
    [InlineKeyboardButton(text='Внутри Анталии ', callback_data='inside_antalya_ru')],
    [InlineKeyboardButton(text='Кемер-Гойнюк-Бельдиби 55$', callback_data='Kemer_Goynuk_Beldibi_ru')],
    [InlineKeyboardButton(text='Белек 45$', callback_data='Belek_ru')],
    [InlineKeyboardButton(text='Сиде 50$', callback_data='Side_ru')],
    [InlineKeyboardButton(text='Манавгат 60$', callback_data='Manavgat_ru')],
    [InlineKeyboardButton(text='Аланья 80$', callback_data='Alanya_ru')],
    [InlineKeyboardButton(text='Текирова-Чамьюва 70$', callback_data='Tekirova_Chamyuva_ru')],
    [InlineKeyboardButton(text='Махмутлар 90$', callback_data='Mahmutlar_ru')]
]

choice_inside_antalya_ru_kb = InlineKeyboardMarkup(inline_keyboard=choice_inside_antalya_button)

location_share_button = [
    [KeyboardButton(text="Поделиться геолокацией", request_location=True)]
]

location_share_kb_ru = ReplyKeyboardMarkup(keyboard=location_share_button, resize_keyboard=True, one_time_keyboard=True)

transfer_about_button_en = [
    [InlineKeyboardButton(text='🔍Learn about the transfer', callback_data='transfer_about_en')]
]

transfer_about_en_kb = InlineKeyboardMarkup(inline_keyboard=transfer_about_button_en)

pick_direction_button_en = [
    [InlineKeyboardButton(text='🗺️Choose a direction', callback_data='pick_direction_en')]
]

pick_direction_en_kb = InlineKeyboardMarkup(inline_keyboard=pick_direction_button_en)

choice_inside_antalya_button_en = [
    [InlineKeyboardButton(text='Inside Antalya', callback_data='inside_antalya_en')],
    [InlineKeyboardButton(text='Kemer-Goynuk-Beldibi 55$', callback_data='Kemer_Goynuk_Beldibi_en')],
    [InlineKeyboardButton(text='Belek 45$', callback_data='Belek_en')],
    [InlineKeyboardButton(text='Side 50$', callback_data='Side_en')],
    [InlineKeyboardButton(text='Manavgat 60$', callback_data='Manavgat_en')],
    [InlineKeyboardButton(text='Alanya 80$', callback_data='Alanya_en')],
    [InlineKeyboardButton(text='Tekirova-Camyuva 70$', callback_data='Tekirova_Chamyuva_en')],
    [InlineKeyboardButton(text='Mahmutlar 90$', callback_data='Mahmutlar_en')]
]

choice_inside_antalya_en_kb = InlineKeyboardMarkup(inline_keyboard=choice_inside_antalya_button_en)

location_share_button_en = [
    [KeyboardButton(text="Share geolocation", request_location=True)]
]

location_share_kb_en = ReplyKeyboardMarkup(keyboard=location_share_button_en, resize_keyboard=True, one_time_keyboard=True)

transfer_about_button_tr = [
    [InlineKeyboardButton(text='🔍Transfer hakkında bilgi edinin', callback_data='transfer_about_en')]
]

transfer_about_tr_kb = InlineKeyboardMarkup(inline_keyboard=transfer_about_button_tr)

pick_direction_button_tr = [
    [InlineKeyboardButton(text='🗺️Bir yön seçin', callback_data='pick_direction_tr')]
]

pick_direction_tr_kb = InlineKeyboardMarkup(inline_keyboard=pick_direction_button_tr)

choice_inside_antalya_button_tr = [
    [InlineKeyboardButton(text="Antalya'nın İçinde ", callback_data='inside_antalya_tr')],
    [InlineKeyboardButton(text='Kemer-Göynük-Beldibi 55$', callback_data='Kemer_Goynuk_Beldibi_tr')],
    [InlineKeyboardButton(text='Belek 45$', callback_data='Belek_tr')],
    [InlineKeyboardButton(text='Yan 50$', callback_data='Side_en')],
    [InlineKeyboardButton(text='Managwat 60$', callback_data='Manavgat_tr')],
    [InlineKeyboardButton(text='Alanya 80$', callback_data='Alanya_tr')],
    [InlineKeyboardButton(text='Tekirova-Chamyuva 70$', callback_data='Tekirova_Chamyuva_tr')],
    [InlineKeyboardButton(text='Mahmutlar 90$', callback_data='Mahmutlar_tr')]
]

choice_inside_antalya_tr_kb = InlineKeyboardMarkup(inline_keyboard=choice_inside_antalya_button_tr)

location_share_button_tr = [
    [KeyboardButton(text="Coğrafi konumu paylaş", request_location=True)]
]

location_share_kb_tr = ReplyKeyboardMarkup(keyboard=location_share_button_tr, resize_keyboard=True, one_time_keyboard=True)
