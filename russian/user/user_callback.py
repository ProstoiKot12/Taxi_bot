import re

from aiogram.types import CallbackQuery, Message, InputMediaPhoto, FSInputFile
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from russian.keyboards.user_keyboards import transfer_about_ru_kb, pick_direction_ru_kb, choice_inside_antalya_ru_kb, \
                                             location_share_kb_ru, transfer_about_en_kb, pick_direction_en_kb,  \
                                             choice_inside_antalya_en_kb, location_share_kb_en, pick_direction_tr_kb, \
                                             choice_inside_antalya_tr_kb, location_share_kb_tr
from utils.sql_request import insert_user_language, insert_user_info, is_language
from config import CHAT_ID


class Form_ru(StatesGroup):
    Kemer_Goynuk_Beldibi_phone_ru = State()
    Kemer_Goynuk_Beldibi_location_ru = State()
    Kemer_Goynuk_Beldibi_done_ru = State()

    Belek_en_phone_ru = State()
    Belek_en_location_ru = State()
    Belek_en_done_ru = State()

    Side_en_phone_ru = State()
    Side_en_location_ru = State()
    Side_en_done_ru = State()

    Manavgat_en_phone_ru = State()
    Manavgat_en_location_ru = State()
    Manavgat_en_done_ru = State()

    Alanya_en_phone_ru = State()
    Alanya_en_location_ru = State()
    Alanya_en_done_ru = State()

    Mahmutlar_en_phone_ru = State()
    Mahmutlar_en_location_ru = State()
    Mahmutlar_en_done_ru = State()

    Tekirova_Chamyuva_en_phone_ru = State()
    Tekirova_Chamyuva_en_location_ru = State()
    Tekirova_Chamyuva_en_done_ru = State()

    inside_antalya_phone_ru = State()
    inside_antalya_location_ru = State()
    inside_antalya_done_ru = State()


name = ''
number_phone = 0
location = ''
phone_pattern = r"\+\d{11}"
pattern = r"\+\d{12}"

async def select_language_russian(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer('')
    user_state = await state.get_state()

    if user_state == 'started':

        await insert_user_language('русский', call.from_user.id)

        await insert_user_language('turkey', call.from_user.id)
        photo_1 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_1.jpg'))
        photo_2 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_2.jpg'))
        photo_3 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_3.jpg'))
        media = [photo_1, photo_2, photo_3]
        await bot.send_media_group(call.from_user.id, media=media)

        await call.message.answer('<b>Добро пожаловать в наш сервис трансфера в Анталии!</b>🥰\n\n'
                                 'Мы готовы предложить вам комфортные поездки, надежные водители и оперативное обслуживание.\n'
                                 'Закажите трансфер с нами и наслаждайтесь удобством и безопасностью во время вашего пребывания в этом прекрасном городе.\n\n'
                                 '<b>Приятного путешествия! </b>🚖✨\n\n'
                                 'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                                 'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=pick_direction_ru_kb)

        await state.set_state("close")
    else:
        language = await is_language(call.from_user.id)

        if language == 'русский':
            await call.message.answer('Ты уже выбрал язык')
        elif language == 'english':
            await call.message.answer('You have already chosen the language')
        elif language == 'turkey':
            await call.message.answer('Zaten bir dil seçtiniz!')

async def select_language_turkey(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer('')
    user_state = await state.get_state()

    if user_state == 'started':

        await insert_user_language('turkey', call.from_user.id)
        photo_1 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_1.jpg'))
        photo_2 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_2.jpg'))
        photo_3 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_3.jpg'))
        media = [photo_1, photo_2, photo_3]
        await bot.send_media_group(call.from_user.id, media=media)
        await call.message.answer("<b>Antalya'daki transfer hizmetimize hoş geldiniz!</b>🥰\n\n"
                                 'Size konforlu seyahat, güvenilir sürücüler ve hızlı hizmet sunmaya hazırız.\n'
                                 'Bizimle bir transfer rezervasyonu yapın ve bu güzel şehirde konaklamanızın rahatlığının ve güvenliğinin tadını çıkarın.\n\n'
                                 '<b>İyi yolculuklar! </b>🚖✨\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=pick_direction_tr_kb)

        await state.set_state("close")
    else:
        language = await is_language(call.from_user.id)

        if language == 'русский':
            await call.message.answer('Ты уже выбрал язык!')
        elif language == 'english':
            await call.message.answer('You have already chosen the language!')
        elif language == 'turkey':
            await call.message.answer('Zaten bir dil seçtiniz!')

async def select_language_english(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer('')
    user_state = await state.get_state()

    if user_state == 'started':
        await insert_user_language('english', call.from_user.id)

        await insert_user_language('turkey', call.from_user.id)
        photo_1 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_1.jpg'))
        photo_2 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_2.jpg'))
        photo_3 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_3.jpg'))
        media = [photo_1, photo_2, photo_3]
        await bot.send_media_group(call.from_user.id, media=media)

        await call.message.answer('<b>Welcome to our transfer service in Antalya!</b>🥰\n\n'
                                 'We are ready to offer you comfortable trips, reliable drivers and prompt service.\n'
                                 'Book a transfer with us and enjoy convenience and safety during your stay in this beautiful city.\n\n'
                                 '<b>Have a great trip! </b>🚖✨\n\n'
                                 'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                                 'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=pick_direction_en_kb)
        await state.set_state("close")
    else:
        language = await is_language(call.from_user.id)

        if language == 'русский':
            await call.message.answer('Ты уже выбрал язык')
        elif language == 'english':
            await call.message.answer('You have already chosen the language')
        elif language == 'turkey':
            await call.message.answer('Zaten bir dil seçtiniz!')

async def transfer_about_ru(call: CallbackQuery):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('<b>С удовольствием предоставляем информацию о тарифах на трансфер в пределах Анталии.</b>🔎\n'
                                  'Согласно нашим условиям, стоимость составляет <b>12.5 лир</b> за каждый пройденный километр.\n\n'
                                  'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                                  'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=pick_direction_ru_kb)
    elif language == 'english':
        await call.message.answer(
            '<b>We are happy to provide information on transfer rates within Antalya.</b>🔎\n'
            'According to our conditions, the cost is <b>12.5 liras</b> per kilometer traveled.\n\n'
            'We can arrange transfers from anywhere in Antalya and its suburbs\n'
            'If you have any questions about transfers, please contact our manager @gotransfer_manager',
            reply_markup=pick_direction_en_kb)
    elif language == 'turkey':
        await call.message.answer(
            '<b>We are happy to provide information on transfer rates within Antalya.</b>🔎\n'
            'According to our conditions, the cost is <b>12.5 liras</b> per kilometer traveled.\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin',
            reply_markup=pick_direction_tr_kb)

async def pick_direction_ru(call: CallbackQuery):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Вот все доступные маршруты\n\n'
                                  'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                                  'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=choice_inside_antalya_ru_kb)
    elif language == 'english':
        await call.message.answer('Here are all available routes\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=choice_inside_antalya_en_kb)
    elif language == 'turkey':
        await call.message.answer('İşte mevcut tüm rotalar\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=choice_inside_antalya_tr_kb)

async def Kemer_Goynuk_Beldibi_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Kemer_Goynuk_Beldibi_phone_ru)

async def Kemer_Goynuk_Beldibi_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Kemer_Goynuk_Beldibi_location_ru)

async def Kemer_Goynuk_Beldibi_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Kemer_Goynuk_Beldibi_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Kemer_Goynuk_Beldibi_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Kemer_Goynuk_Beldibi_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Kemer_Goynuk_Beldibi_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Кемер-Гойнюк-Бельдиби</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Belek_en(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Belek_en_phone_ru)

async def Belek_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Belek_en_location_ru)

async def Belek_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Belek_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Belek_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Belek_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Belek_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Белек</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Side_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Side_en_phone_ru)

async def Side_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Side_en_location_ru)

async def Side_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Side_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Side_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Side_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Side_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Сиде</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Manavgat_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Manavgat_en_phone_ru)

async def Manavgat_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Manavgat_en_location_ru)

async def Manavgat_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Manavgat_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Manavgat_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Manavgat_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Manavgat_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Манагват</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Alanya_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Alanya_en_phone_ru)

async def Alanya_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Alanya_en_location_ru)

async def Alanya_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Alanya_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Alanya_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Alanya_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Alanya_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Аланья</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Mahmutlar_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Mahmutlar_en_phone_ru)

async def Mahmutlar_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Mahmutlar_en_location_ru)

async def Mahmutlar_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Mahmutlar_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Mahmutlar_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Mahmutlar_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Mahmutlar_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер:\n'
                                     f'<b>Махмутлар</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def inside_antalya(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('<b>С удовольствием предоставляем информацию о тарифах на трансфер в пределах Анталии.</b>🔎\n'
                                  'Согласно нашим условиям, стоимость составляет <b>12.5 лир</b> за каждый пройденный километр.\n\n'
                                  'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                                  'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager')
        await call.message.answer('Введите ваше имя')
    elif language == 'english':
        await call.message.answer('<b>We are happy to provide information on transfer rates within Antalya.</b>🔎\n'
                                  'According to our conditions, the cost is <b>12.5 liras</b> per kilometer traveled.\n\n'
                                  'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                                  'If you have any questions about transfers, please contact our manager @gotransfer_manager')
        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('<b>Antalya içi transfer ücretleri hakkında bilgi vermekten mutluluk duyarız.</b>🔎\n'
                                  'Hüküm ve koşullarımıza göre, kat edilen kilometre başına <b>12,5 lira</b> ücret alınmaktadır.\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin')
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.inside_antalya_phone_ru)

async def inside_antalya_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Mahmutlar_en_location_ru)

async def inside_antalya_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.inside_antalya_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.inside_antalya_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.inside_antalya_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def inside_antalya_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка\n'
                                     f'<b>Внутри Анталии</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")

async def Tekirova_Chamyuva_ru(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    language = await is_language(call.from_user.id)

    if language == 'русский':
        await call.message.answer('Введите ваше имя')
    elif language == 'english':

        await call.message.answer('Enter your name')
    elif language == 'turkey':
        await call.message.answer('Adınızı girin')

    await state.set_state(Form_ru.Tekirova_Chamyuva_en_phone_ru)

async def Tekirova_Chamyuva_en_phone_ru(message: Message, state: FSMContext):
    global name
    name = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        await message.answer('Введите свой номер телефона')
    elif language == 'english':
        await message.answer('Enter your phone number')
    elif language == 'turkey':
        await message.answer('Telefon numaranızı girin')

    await state.set_state(Form_ru.Tekirova_Chamyuva_en_location_ru)

async def Tekirova_Chamyuva_en_location_ru(message: Message, state: FSMContext):
    global number_phone
    number_phone = message.text.strip()
    language = await is_language(message.from_user.id)

    if language == 'русский':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Поделитесь своей геолокацией', reply_markup=location_share_kb_ru)
            await state.set_state(Form_ru.Tekirova_Chamyuva_en_done_ru)
        else:
            await message.answer('Номер телефона должен соответствовать формату +71234567890 или +900000000000')
    elif language == 'english':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Share your geolocation', reply_markup=location_share_kb_en)
            await state.set_state(Form_ru.Tekirova_Chamyuva_en_done_ru)
        else:
            await message.answer('The phone number must be in the format +71234567890 or +900000000000')
    elif language == 'turkey':
        if re.match(phone_pattern, number_phone) or re.fullmatch(pattern, number_phone):
            await message.answer('Coğrafi konumunuzu paylaşın', reply_markup=location_share_kb_tr)
            await state.set_state(Form_ru.Tekirova_Chamyuva_en_done_ru)
        else:
            await message.answer('Telefon numarası +71234567890, +900000000000 biçiminde olmalıdır')

async def Tekirova_Chamyuva_en_done_ru(message: Message, state: FSMContext, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Ширина: {}\nДолгота: {}".format(f'<code>{lat}</code>', f'<code>{lon}</code>')
    reply_for_sql = "Ширина: {}\nДолгота: {}".format(lat, lon)
    language = await is_language(message.from_user.id)

    await insert_user_info(message.from_user.id, message.from_user.username, name, number_phone, reply_for_sql)

    await bot.send_message(CHAT_ID, f'Была оставлена заявка на трансфер\n'
                                     f'<b>Текирова-Чамьюва</b>\n'
                                     f'Имя: <b>{name}</b>\n'
                                     f'Номер телефона: <code>{number_phone}</code>\n'
                                     f'Телеграмм: @{message.from_user.username}\n'
                                     f'{reply}')
    if language == 'русский':
        await message.answer('Отлично, заявка была оставлена\n'
                             'Чтобы еще выбрать направления введите команду /transfers\n\n'
                             'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                             'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'english':
        await message.answer('Great, the application has been left\n'
                             'To select more destinations, enter the /transfers command\n\n'
                             'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                             'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
    elif language == 'turkey':
        await message.answer('Harika, uygulama bırakıldı\n'
                             'Daha fazla hedef seçmek için /transfers komutunu girin\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=ReplyKeyboardRemove())
        await state.set_state("close")
