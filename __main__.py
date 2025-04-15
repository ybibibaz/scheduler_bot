import asyncio

from aiogram import Bot

from commands import *  # this line links commands to dispatcher, don't remove
from conf import SettingsConfig
from dispatcher import SingletonDispatcher


async def main():
    bot_settings = SettingsConfig.from_local_config()
    bot = Bot(token=bot_settings.token)
    await SingletonDispatcher().start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
