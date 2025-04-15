import textwrap

from aiogram.filters.command import Command

from dispatcher import SingletonDispatcher


GREET_MESSAGE = 'Hello! Welcome to the greatest(!!!) of schedule bots!\n\n'
HELP_MESSAGE = textwrap.dedent('''
    Commands list:

    /help - Show this message
    /add_event - Add event. Use one of formats: DD.MM.YYYY <event> '''
    '''i.e. `24.04.2024 very important meeting` for single time event '''
    '''| DD <event> i.e. `1 choose cashbacks` for monthly regular event.
''').strip()


@SingletonDispatcher().message(Command("start"))
async def cmd_start(message):
    await message.answer(GREET_MESSAGE + HELP_MESSAGE)


@SingletonDispatcher().message(Command("help"))
async def cmd_help(message):
    await message.answer(HELP_MESSAGE)
