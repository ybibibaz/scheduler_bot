import re

EVENT_FORMATS_MESSAGE = textwrap.dedent('''
    - HH:MM DD.MM.YYYY <event> - simple event.
    - HH:MM DD.MM <event> - simple event (use current year as year).
    - DD <event> - monthly event. Triggers every DD of each month. '''
    '''Uses last day of month if DD is larger then the number of days in month.
    - <day of the week> <event> - weekly event.
    - HH:MM <day of the week> <event> - weekly event with time.
''').strip()
EVENT_FORMATS = [
    SIMPLE_EVENT,
    SIMPLE_EVENT_WITHOUT_YEAR,
] = [
    re.compile(r'^(?P<time>(\d)|(\d\d):\d\d)\s+(?P<date>(\d\d\.\d\d\.\d\d\d\d))\s+(?P<event>.*)$'),
    re.compile(r'^(?P<time>(\d)|(\d\d):\d\d)\s+(?P<date>(\d\d\.\d\d))\s+(?P<event>.*)$'),
]