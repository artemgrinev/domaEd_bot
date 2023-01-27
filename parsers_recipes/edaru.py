import requests
from bs4 import BeautifulSoup


def get_ingredients(url: str) -> tuple:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    recipes_name = soup.select('span[itemprop = "name"] > h1')[0].text
    ingredients = soup.find_all('div', class_="emotion-ydhjlb")
    data = {}
    for i in ingredients:
        name = i.find('span', itemprop='recipeIngredient')
        mes = i.find('span', class_='emotion-15im4d2')
        if name and mes:
            data.update({name.text: mes.text})
    # Пока нет нормальной обработки хроню строку потом буду возврощать словарь
    ingredients_str = ''
    for k, v in data.items():
        ingredients_str += f'{k} - {v}\n'
    return recipes_name, ingredients_str
