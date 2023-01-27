from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from db.config_db import DATABASE
from db.tables import Base, Users, Recipes, ActionsUsers
from parsers_recipes.edaru import get_ingredients


def create_session_db():
    engine = create_engine(URL.create(**DATABASE))
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    session = create_session()
    return session


def get_recipes(url: str) -> tuple:
    new_session = create_session_db()
    assert isinstance(url, str)
    recipes = new_session.query(Recipes).filter(Recipes.link == url).value(Recipes.ingredients)
    name = new_session.query(Recipes).filter(Recipes.link == url).value(Recipes.name)
    if recipes:
        return name, recipes
    else:
        name, ingredients = get_ingredients(url)

        data = Recipes(
            name=name,
            link=url,
            ingredients=ingredients,
        )
        new_session.add(data)
        new_session.commit()
        print(f'create new recipes {name}')
        return name, ingredients


def get_user(user_id, last_name, first_name):
    new_session = create_session_db()
    assert isinstance(user_id, int)
    id_ = new_session.query(Users).filter(Users.user_id == user_id).value(Users.id)
    print(id_)
    if id_ is None:
        data = Users(
            user_id=user_id,
            last_name=last_name,
            first_name=first_name,
        )
        new_session.add(data)

        new_session.commit()
        id_ = new_session.query(Users).filter(Users.user_id == user_id).value(Users.id)
        print(f'create new user {id_}')
    actions = ActionsUsers(
        user_id=id_
    )
    new_session.add(actions)
    new_session.commit()
    print(f'user {id_} is active')


