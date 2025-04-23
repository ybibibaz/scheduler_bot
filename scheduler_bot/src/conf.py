import dataclasses
import json
import pathlib


SETTINGS_CONFIG_PATH = pathlib.Path(__file__).parent / 'configs' / 'settings.json'
CONFIG_EXAMPLE = {
    'token': 'Telegram bot token',
}

@dataclasses.dataclass
class SettingsConfig:
    token: str
    user_id: int

    @classmethod
    def from_local_config(cls):
        with SETTINGS_CONFIG_PATH.open() as f:
            config = json.load(f)
        return cls(**config)
