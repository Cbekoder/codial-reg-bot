from asyncio import run
import logging
import sys
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import bot, dp, db
import handlers

async def on_startup():
    await on_startup_notify()
    await set_default_commands()
    db.create_user_table()

async def main() -> None:
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(main())
