import asyncio

from aiogram import Bot

from scheduler_bot.src.commands import *  # this line links commands to dispatcher, don't remove
from scheduler_bot.src.conf import SettingsConfig
from scheduler_bot.src.dispatcher import SingletonDispatcher


async def main():
    bot_settings = SettingsConfig.from_local_config()
    bot = Bot(token=bot_settings.token)
    dispatcher = SingletonDispatcher()
    dispatcher.set_user_id(bot_settings.user_id)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
