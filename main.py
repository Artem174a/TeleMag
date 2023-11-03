import asyncio
from bot.main import main as bot_main
from loging import *
from conf import config


if __name__ == '__main__':
    start_log()
    asyncio.run(bot_main())
