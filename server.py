import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
#load env variables 
load_dotenv()

app = Flask(__name__)
#set environtment 
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODFICATIONS']=False
db= SQLAlchemy(app)

from models import Result
#print env to console
print(os.environ['APP_SETTINGS'])

@app.route("/")
def hello():
  return "My name is HAL"

if __name__ == '__main__':
  app.run()