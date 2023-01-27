from aiogram import Bot, Dispatcher, executor, types

from db.conect_db import get_user, get_recipes

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
    user_id = message.from_user.id
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name
    get_user(user_id, last_name, first_name)
    if url.split('/')[0] != "https:":
        await message.answer('Сообщение должно содержать https:')
    elif url.split('/')[2] != "eda.ru":
        await message.answer('Извини, я пока умею работать только с рецептами сайта eda.ru')
    else:
        name, ingredients = get_recipes(url)
        await message.answer(ingredients)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
