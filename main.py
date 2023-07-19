import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN, ADMIN_ID
from utils.sql_request import create_table
from utils.commands import set_commands
from russian.user.user_handlers import start_select_language, pick_direction_command_ru
from russian.user.user_callback import select_language_russian, transfer_about_ru, pick_direction_ru, \
                                       Kemer_Goynuk_Beldibi_phone_ru, Kemer_Goynuk_Beldibi_ru, \
                                       Kemer_Goynuk_Beldibi_location_ru, Kemer_Goynuk_Beldibi_done_ru, Form_ru, \
                                       select_language_english, Belek_en_done_ru, Belek_en_phone_ru, \
                                       Belek_en, Side_en_done_ru, Side_en_phone_ru, Side_en_location_ru, Side_ru, \
                                       Manavgat_ru, Manavgat_en_phone_ru, Manavgat_en_done_ru, Manavgat_en_location_ru, \
                                       Alanya_ru, Alanya_en_done_ru, Alanya_en_phone_ru, Alanya_en_location_ru, \
                                       Mahmutlar_en_location_ru, Mahmutlar_ru, Mahmutlar_en_done_ru, \
                                       Mahmutlar_en_phone_ru, Belek_en_location_ru, inside_antalya_phone_ru, \
                                       inside_antalya_done_ru, inside_antalya_location_ru, inside_antalya, \
                                       select_language_turkey, Tekirova_Chamyuva_ru, Tekirova_Chamyuva_en_done_ru, \
                                       Tekirova_Chamyuva_en_location_ru, Tekirova_Chamyuva_en_phone_ru


router = Router()

async def start_bot(bot: Bot):
    await set_commands(bot)
    await create_table()
    await bot.send_message(ADMIN_ID, text='Бот запущен!')

async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")

    dp.startup.register(start_bot)

    dp.message.register(start_select_language, Command('start'))
    dp.message.register(pick_direction_command_ru, Command('transfers'))

    dp.message.register(Tekirova_Chamyuva_en_phone_ru, Form_ru.Tekirova_Chamyuva_en_phone_ru)
    dp.message.register(Tekirova_Chamyuva_en_location_ru, Form_ru.Tekirova_Chamyuva_en_location_ru)
    dp.message.register(Tekirova_Chamyuva_en_done_ru, Form_ru.Tekirova_Chamyuva_en_done_ru)

    dp.message.register(inside_antalya_phone_ru, Form_ru.inside_antalya_phone_ru)
    dp.message.register(inside_antalya_location_ru, Form_ru.inside_antalya_location_ru)
    dp.message.register(inside_antalya_done_ru, Form_ru.inside_antalya_done_ru)

    dp.message.register(Kemer_Goynuk_Beldibi_phone_ru, Form_ru.Kemer_Goynuk_Beldibi_phone_ru)
    dp.message.register(Kemer_Goynuk_Beldibi_location_ru, Form_ru.Kemer_Goynuk_Beldibi_location_ru)
    dp.message.register(Kemer_Goynuk_Beldibi_done_ru, Form_ru.Kemer_Goynuk_Beldibi_done_ru)

    dp.message.register(Belek_en_location_ru, Form_ru.Belek_en_location_ru)
    dp.message.register(Belek_en_phone_ru, Form_ru.Belek_en_phone_ru)
    dp.message.register(Belek_en_done_ru, Form_ru.Belek_en_done_ru)

    dp.message.register(Side_en_phone_ru, Form_ru.Side_en_phone_ru)
    dp.message.register(Side_en_location_ru, Form_ru.Side_en_location_ru)
    dp.message.register(Side_en_done_ru, Form_ru.Side_en_done_ru)

    dp.message.register(Manavgat_en_phone_ru, Form_ru.Manavgat_en_phone_ru)
    dp.message.register(Manavgat_en_done_ru, Form_ru.Manavgat_en_done_ru)
    dp.message.register(Manavgat_en_location_ru, Form_ru.Manavgat_en_location_ru)

    dp.message.register(Alanya_en_phone_ru, Form_ru.Alanya_en_phone_ru)
    dp.message.register(Alanya_en_location_ru, Form_ru.Alanya_en_location_ru)
    dp.message.register(Alanya_en_done_ru, Form_ru.Alanya_en_done_ru)

    dp.message.register(Mahmutlar_en_done_ru, Form_ru.Mahmutlar_en_done_ru)
    dp.message.register(Mahmutlar_en_location_ru, Form_ru.Mahmutlar_en_location_ru)
    dp.message.register(Mahmutlar_en_phone_ru, Form_ru.Mahmutlar_en_phone_ru)

    dp.callback_query.register(select_language_russian, F.data.startswith('select_language_russian'))
    dp.callback_query.register(select_language_english, F.data.startswith('select_language_english'))
    dp.callback_query.register(select_language_turkey, F.data.startswith('select_language_turkey'))
    dp.callback_query.register(transfer_about_ru, F.data.startswith('transfer_about_ru'))
    dp.callback_query.register(pick_direction_ru, F.data.startswith('pick_direction_ru'))

    dp.callback_query.register(transfer_about_ru, F.data.startswith('transfer_about_en'))
    dp.callback_query.register(pick_direction_ru, F.data.startswith('pick_direction_en'))

    dp.callback_query.register(transfer_about_ru, F.data.startswith('transfer_about_tr'))
    dp.callback_query.register(pick_direction_ru, F.data.startswith('pick_direction_tr'))

    dp.callback_query.register(Kemer_Goynuk_Beldibi_ru, F.data.startswith('Kemer_Goynuk_Beldibi_en'))
    dp.callback_query.register(Kemer_Goynuk_Beldibi_ru, F.data.startswith('Kemer_Goynuk_Beldibi_ru'))
    dp.callback_query.register(Kemer_Goynuk_Beldibi_ru, F.data.startswith('Kemer_Goynuk_Beldibi_tr'))
    dp.callback_query.register(Belek_en, F.data.startswith('Belek_en'))
    dp.callback_query.register(Belek_en, F.data.startswith('Belek_ru'))
    dp.callback_query.register(Belek_en, F.data.startswith('Belek_tr'))
    dp.callback_query.register(Side_ru, F.data.startswith('Side_ru'))
    dp.callback_query.register(Side_ru, F.data.startswith('Side_en'))
    dp.callback_query.register(Side_ru, F.data.startswith('Side_tr'))
    dp.callback_query.register(Manavgat_ru, F.data.startswith('Manavgat_ru'))
    dp.callback_query.register(Manavgat_ru, F.data.startswith('Manavgat_en'))
    dp.callback_query.register(Manavgat_ru, F.data.startswith('Manavgat_tr'))
    dp.callback_query.register(Alanya_ru, F.data.startswith('Alanya_ru'))
    dp.callback_query.register(Alanya_ru, F.data.startswith('Alanya_en'))
    dp.callback_query.register(Alanya_ru, F.data.startswith('Alanya_tr'))
    dp.callback_query.register(Mahmutlar_ru, F.data.startswith('Mahmutlar_ru'))
    dp.callback_query.register(Mahmutlar_ru, F.data.startswith('Mahmutlar_en'))
    dp.callback_query.register(Mahmutlar_ru, F.data.startswith('Mahmutlar_tr'))
    dp.callback_query.register(Tekirova_Chamyuva_ru, F.data.startswith('Tekirova_Chamyuva_ru'))
    dp.callback_query.register(Tekirova_Chamyuva_ru, F.data.startswith('Tekirova_Chamyuva_en'))
    dp.callback_query.register(Tekirova_Chamyuva_ru, F.data.startswith('Tekirova_Chamyuva_tr'))
    dp.callback_query.register(inside_antalya, F.data.startswith('inside_antalya_ru'))
    dp.callback_query.register(inside_antalya, F.data.startswith('inside_antalya_en'))
    dp.callback_query.register(inside_antalya, F.data.startswith('inside_antalya_tr'))

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
