from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB
db = SQLAlchemy(app)
import models


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def test_app():
    return "Test result"

if __name__ == "__main__":
    app.run()
