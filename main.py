import asyncio
from functools import partial

from Aplication.main import main
from bot.main import main as bot_main
from database.main import DB
from loging import *
import flet as ft
from conf import config


if __name__ == '__main__':
    # start_log()
    # asyncio.run(bot_main())
    try:
        ft.app(target=main, view=ft.WEB_BROWSER)
    except Exception as e:
        print(f'Error - {e}')
