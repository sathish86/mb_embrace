from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from factual import Factual
from factual.utils import circle
import settings
import constants
from geo_points import GeoPoints
from base_exception import LocationEmptyError, NoResultFound

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB
db = SQLAlchemy(app)
import models


def error_response(err_msg):
    """
    Accept error message data
    :param err_msg: error message from the exception
    :return: list: json dict with error message
    """
    return [{'error_message': err_msg}]


class FindShopsResource(Resource):

    def get(self):
        """
        Get location and type of the cuisine and return the response based on geo coordinate points using GOOGLE MAP API
        :return: list: response in json dictionary with result
        """
        try:
            location = request.values.get("location")
            type_val = request.values.get("type")

            if not location or not type_val:
                return {'result': {'error': 'parameters location or type is missing'}}
            else:
                # initialise factual object
                factual = Factual(settings.FACTUAL_API_KEY, settings.FACTUAL_API_SECRET)
                factual_table_data = factual.table(constants.API_ENDPOINT)
                # find geo points
                obj_geo = GeoPoints(location)
                lat, lng = obj_geo.find_geo_points()
                # filter based on geo points and type of the cuisine type with a distance in ascending order.
                data = factual_table_data.geo(circle(lat, lng, constants.GEO_CIRCLE_DISTANCE_METER)).sort_asc('$distance')\
                    .filters({'cuisine': type_val}).limit(constants.RESULT_LIMIT).data()
                return data
        except LocationEmptyError as e:
            return error_response(e)
        except NoResultFound as e:
            return error_response(e)
        except Exception as e:
            error_message = "something went wrong, please contact support team"
            return error_response(error_message)


class RecommendationResource(Resource):
    def post(self):
        """
        Get location and type of the cuisine and return the response based on geo coordinate points using GOOGLE MAP API
        :return: list: response in json dictionary with result
        """
        location = request.values.get("location")


api.add_resource(FindShopsResource, '/find')
api.add_resource(RecommendationResource, '/recommend')

if __name__ == "__main__":
    app.run(debug=True)
