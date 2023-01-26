from aiogram import Bot, Dispatcher, executor, types
from parsers.edaru import get_ingredients

from configurations import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ ДомаEd-бот!\nОтправь мне любую ссылку на рецепт с сайта https://eda.ru/,"
                        " а я скажу сколько он тебе обойдется в магазине О'кей.")


@dp.message_handler()
async def echo(message: types.Message):
    url = message.text
    d = get_ingredients(url)
    ingredients_str = ''
    for k, v in d.items():
        ingredients_str += f'{k} - {v}\n'
    await message.answer(ingredients_str)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
