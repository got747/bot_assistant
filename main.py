import bookkeeping
from aiohttp import web
from loader import dp, executor 

async def on_startup(web_app: web.Application):
    await bookkeeping.setup(dp)


async def on_shutdown(web_app: web.Application):
    await dp.storage.close()
    await dp.storage.wait_closed()


def main():
    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)
    executor.start_polling()

if __name__ == '__main__':
    main()