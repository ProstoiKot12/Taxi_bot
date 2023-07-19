from aiogram.types import Message, InputFile, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot

from russian.keyboards.user_keyboards import select_language_kb, transfer_about_ru_kb, \
                                             choice_inside_antalya_ru_kb, choice_inside_antalya_en_kb, \
                                             transfer_about_en_kb, pick_direction_ru_kb, pick_direction_en_kb, \
                                             pick_direction_tr_kb, choice_inside_antalya_tr_kb


from utils.sql_request import is_language

async def start_select_language(message: Message, state: FSMContext, bot: Bot):
    user_state = await state.get_state()

    if user_state is None:
        await message.answer('<b>Select a language</b>', reply_markup=select_language_kb)

        await state.set_state("started")
    else:
        photo_1 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_1.jpg'))
        photo_2 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_2.jpg'))
        photo_3 = InputMediaPhoto(type='photo',
                                  media=FSInputFile(r'photo_3.jpg'))
        media = [photo_1, photo_2, photo_3]
        language = await is_language(message.from_user.id)
        if language == 'русский':
            await bot.send_media_group(message.from_user.id, media=media)
            await message.answer('<b>Добро пожаловать в наш сервис трансфера в Анталии!</b>🥰\n\n'
                                              'Мы готовы предложить вам комфортные поездки, надежные водители и оперативное обслуживание.\n'
                                              'Закажите трансфер с нами и наслаждайтесь удобством и безопасностью во время вашего пребывания в этом прекрасном городе.\n\n'
                                              '<b>Приятного путешествия! </b>🚖✨\n\n'
                                              'Мы можем вам организовать трансфер с любой точки Анталии и ее пригородах\n'
                                              'По всем вопросам по поводу трансфера обращаться к менеджеру @gotransfer_manager', reply_markup=pick_direction_ru_kb)

        elif language == 'english':
            await bot.send_media_group(message.from_user.id, media=media)
            await message.answer('<b>Welcome to our transfer service in Antalya!</b>🥰\n\n'
                                 'We are ready to offer you comfortable trips, reliable drivers and prompt service.\n'
                                 'Book a transfer with us and enjoy convenience and safety during your stay in this beautiful city.\n\n'
                                 '<b>Have a great trip! </b>🚖✨\n\n'
                                 'We can arrange transfers from anywhere in Antalya and its suburbs\n'
                                 'If you have any questions about transfers, please contact our manager @gotransfer_manager', reply_markup=pick_direction_en_kb)
        elif language == 'turkey':
            await bot.send_media_group(message.from_user.id, media=media)
            await message.answer("<b>Antalya'daki transfer hizmetimize hoş geldiniz!</b>🥰\n\n"
                                 'Size konforlu seyahat, güvenilir sürücüler ve hızlı hizmet sunmaya hazırız.\n'
                                 'Bizimle bir transfer rezervasyonu yapın ve bu güzel şehirde konaklamanızın rahatlığının ve güvenliğinin tadını çıkarın.\n\n'
                                 '<b>İyi yolculuklar! </b>🚖✨\n\n'
                                 'Antalya ve banliyölerinin her yerinden transfer ayarlayabiliriz\n'
                                 'Transferler hakkında herhangi bir sorunuz varsa @gotransfer_manager ile iletişime geçin', reply_markup=pick_direction_tr_kb)

async def pick_direction_command_ru(message: Message):
    language = await is_language(message.from_user.id)
    if language == 'русский':
        await message.answer('Вот все доступные маршруты', reply_markup=choice_inside_antalya_ru_kb)
    elif language == 'english':
        await message.answer('Here are all available routes', reply_markup=choice_inside_antalya_en_kb)
    elif language == 'turkey':
        await message.answer('İşte mevcut tüm rotalar', reply_markup=choice_inside_antalya_tr_kb)