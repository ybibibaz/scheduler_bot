import datetime
import re

from scheduler_bot.src import exceptions

"""
EVENT_FORMATS_MESSAGE = textwrap.dedent('''
    DONE: - HH:MM DD.MM.YYYY <event> or DD.MM.YYYY HH:MM <event>- simple event.
    DONE: - HH:MM DD.MM <event> or DD.MM or HH:MM <event> - simple event (use current year as year).
    - DD <event> - monthly event. Triggers every DD of each month. '''
    '''Uses last day of month if DD is larger then the number of days in month.
    - <day of the week> <event> - weekly event.
    - HH:MM <day of the week> <event> - weekly event with time.
''').strip()
"""
TIME_FORMAT = r'((\d)|(\d\d)):\d\d'
DATE_FORMAT = r'((\d)|(\d\d))\.\d\d(\.\d\d\d\d)?'
MESSAGE_FORMATS = [
    SIMPLE_MESSAGE_TIME_FIRST,
    SIMPLE_MESSAGE_DATE_FIRST,
] = [
    re.compile(rf'^\s*(?P<time>{TIME_FORMAT})\s+(?P<date>{DATE_FORMAT})\s+(?P<event>.*)$'),
    re.compile(rf'^\s*(?P<date>{DATE_FORMAT})\s+(?P<time>{TIME_FORMAT})\s+(?P<event>.*)$'),
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
                # Add current year if it's not presented in date
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
