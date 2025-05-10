import textwrap

from aiogram.filters.command import Command

from scheduler_bot.src.dispatcher import SingletonDispatcher


GREET_MESSAGE = 'Hello! Welcome to the greatest(!!!) of schedule bots!\n\n'
HELP_MESSAGE = textwrap.dedent('''
    Commands list:

    /help - Show this message.
    /add_event - Add event. Use command /event_formats to see every possible format of events.
    /event_formats - Show possible formats of events for command /add_event.
    /events - Show all existing events.
    /remove_event - Remove event by its id (number from command /events).
''').strip()
EVENT_FORMATS_MESSAGE = textwrap.dedent('''
    - HH:MM DD.MM.YYYY <event> or DD.MM.YYYY HH:MM <event>- simple event.
    - HH:MM DD.MM <event> or DD.MM or HH:MM <event> - simple event (use current year as year).
    - DD <event> - monthly event. Triggers every DD of each month. '''
    '''Uses last day of month if DD is larger then the number of days in month.
    - <day of the week> <event> - weekly event.
    - HH:MM <day of the week> <event> - weekly event with time.
''').strip()


@SingletonDispatcher().message(Command("start"))
@SingletonDispatcher().check_user_id
async def cmd_start(message):
    await message.answer(GREET_MESSAGE + HELP_MESSAGE)


@SingletonDispatcher().message(Command("help"))
@SingletonDispatcher().check_user_id
async def cmd_help(message):
    await message.answer(HELP_MESSAGE)


@SingletonDispatcher().message(Command("event_formats"))
@SingletonDispatcher().check_user_id
async def cmd_event_formats(message):
    await message.answer(EVENT_FORMATS_MESSAGE)


@SingletonDispatcher().message(Command("add_event"))
@SingletonDispatcher().check_user_id
async def cmd_add_event(message):
    # TODO: parse event formats here
    await message.answer('Work in progress.')
