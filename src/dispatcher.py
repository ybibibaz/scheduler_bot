from aiogram import Dispatcher


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonDispatcher(Dispatcher, metaclass=Singleton):
    def set_user_id(self, user_id):
        self.user_id = user_id

    def check_user_id(self, func):
        async def wrapper(message):
            if message.from_user.id != self.user_id:
                return await message.answer('You have no rights here.')
            await func(message)
        return wrapper
