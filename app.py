import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
# load env variables
load_dotenv()

app = Flask(__name__)
# set environment
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
# import models after instantiation of db
from models import user, outfit, closet, clothing_item, clothing_outfit
# print env to console
print(os.environ['APP_SETTINGS'])


@app.shell_context_processor
def make_shell_context():
    return{
        'db': db,
        'User': user.User,
        'Outfit': outfit.Outfit,
        'Closet': closet.Closet,
        'ClothingItem': clothing_item.ClothingItem,
        'ClothingOutfit': clothing_outfit.ClothingOutfit,
    }


@app.route("/")
def hello():
    return "My name is HAL"


if __name__ == '__main__':
    app.run()
