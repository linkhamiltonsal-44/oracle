import os, asyncio, json
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")   # we’ll use GitHub Secret later
bot = Bot(token=TOKEN)
dp  = Dispatcher()

@dp.message()
async def any_message(message: types.Message):
    data = {
        "date": str(message.date),
        "user": message.from_user.full_name,
        "text": message.text
    }
    print(json.dumps(data, ensure_ascii=False))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
