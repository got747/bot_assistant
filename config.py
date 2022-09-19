
from envparse import env

env.read_envfile()

BOT_TOKEN = env.str("TOKEN_TELEGRAM")
