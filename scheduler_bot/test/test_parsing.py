import datetime

import pytest

from scheduler_bot.src.parse_message import ParsedMessage


@pytest.mark.parametrize(
    ['message', 'fields'],
    (
        (
            '12:00  11.12.2010  event_mock',
            {
                'time': datetime.time(12, 0),
                'date': datetime.date(2010, 12, 11),
                'event': 'event_mock',
            },
        ),
        (
            '12:00  11.12  event_mock',
            {
                'time': datetime.time(12, 0),
                'date': datetime.date(datetime.datetime.now().year, 12, 11),
                'event': 'event_mock',
            },
        ),
        (
            '12:00  1.12.2010  event_mock',
            {
                'time': datetime.time(12, 0),
                'date': datetime.date(2010, 12, 1),
                'event': 'event_mock',
            },
        ),
        (
            '12:00  1.12  event_mock',
            {
                'time': datetime.time(12, 0),
                'date': datetime.date(datetime.datetime.now().year, 12, 1),
                'event': 'event_mock',
            },
        )
    )
)
def test_parse_message(message, fields):
    parsed_message = ParsedMessage.from_message(message)
    for field_name, field_value in fields.items():
        assert getattr(parsed_message, field_name) == field_value
