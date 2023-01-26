import requests
from bs4 import BeautifulSoup


def get_ingredients(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    ingredients = soup.find_all('div', class_="emotion-ydhjlb")
    data = {}
    for i in ingredients:
        name = i.find('span', itemprop='recipeIngredient')
        mes = i.find('span', class_='emotion-15im4d2')
        if name and mes:
            data.update({name.text: mes.text})
    return data
