import datetime
import re

from scheduler_bot.src import exceptions

"""
EVENT_FORMATS_MESSAGE = textwrap.dedent('''
    - HH:MM DD.MM.YYYY <event> - simple event.
    - HH:MM DD.MM <event> - simple event (use current year as year).
    - DD <event> - monthly event. Triggers every DD of each month. '''
    '''Uses last day of month if DD is larger then the number of days in month.
    - <day of the week> <event> - weekly event.
    - HH:MM <day of the week> <event> - weekly event with time.
''').strip()
"""
MESSAGE_FORMATS = [
    SIMPLE_MESSAGE,
    SIMPLE_MESSAGE_WITHOUT_YEAR,
] = [
    re.compile(r'^\s*(?P<time>((\d)|(\d\d)):\d\d)\s+(?P<date>((\d)|(\d\d))\.\d\d\.\d\d\d\d)\s+(?P<event>.*)$'),
    re.compile(r'^\s*(?P<time>((\d)|(\d\d)):\d\d)\s+(?P<date>((\d)|(\d\d))\.\d\d)\s+(?P<event>.*)$'),
]


class ParsedMessage:
    def __init__(
        self,
        *,
        event: str,
        time: str | None = None,
        date: str | None = None,
    ):
        self.event = event
        self.time = None
        self.date = None
        if time:
            try:
                self.time = datetime.datetime.strptime(time, '%H:%M').time()
            except ValueError as e:
                raise exceptions.WrongTimeFormat(e)
        if date:
            try:
                if re.match(r'^((\d)|(\d\d))\.\d\d$', date):
                    date = f'{date}.{datetime.datetime.now().year}'
                self.date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
            except ValueError as e:
                raise exceptions.WrongDateFormat(e)

    @property
    def is_cron_event(self):
        return not self.time or not self.date

    @classmethod
    def from_message(cls, message):
        for event_format in MESSAGE_FORMATS:
            if match_obj := event_format.match(message):
                return cls(**match_obj.groupdict())
