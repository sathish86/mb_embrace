from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from factual import Factual
from factual.utils import circle
import settings
import constants

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB
db = SQLAlchemy(app)
import models


@app.route("/")
def hello():
    print "Hellow"
    factual = Factual(settings.FACTUAL_API_KEY, settings.FACTUAL_API_SECRET)
    rest_data = factual.table(constants.API_ENDPOINT)
    response = rest_data.search('coffee').geo(circle(-33.870400, 151.222300, 1000)).data()
    print response


    return "Hello World!"


@app.route("/test")
def test_app():
    return "Test result"

if __name__ == "__main__":
    app.run()
