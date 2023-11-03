from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loging import logger
from conf import config


def reg_all_handlers(dp):
    # reg_admin_handler(dp, queue, queue_account)
    pass


async def main():
    # Извлечение токена из конфигурационного файла
    token = config['telegram']['token']

    # Подключение к Redis
    storage = RedisStorage2(host=config['redis']['host'], port=int(config['redis']['port']))

    logger.info("Starting bot")

    bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(LoggingMiddleware())

    # Ловим сообщения
    reg_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        # Остановили бота и закрываем сессию
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
