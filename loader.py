from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import Executor

from config import BOT_TOKEN

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot, storage=storage)

executor = Executor(dp)