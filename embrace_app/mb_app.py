from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import uuid
import flask
from flask import request
from flask_restful import Resource
import logging
from factual.utils import circle
from geo_points import GeoPoints
from base_exception import LocationEmptyError, NoResultFound, InputDataError
from recommendation import Recommendation
from factual import Factual
import settings
import constants

logging.basicConfig()
logger = logging.getLogger('MB API Logging')

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB
db = SQLAlchemy(app)


class RecommendationLogging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    title = db.Column(db.String(80))
    likes = db.Column(db.String(200))
    dislikes = db.Column(db.String(200))
    requirements = db.Column(db.String(80))
    group_id = db.Column(db.String(50))

    def __init__(self, name, title, likes, dislikes, requirements, group_id):
        self.name = name
        self.title = title
        self.likes = likes
        self.dislikes = dislikes
        self.requirements = requirements
        self.group_id = group_id

    def __repr__(self):
        return '<User %r>' % self.name


# create database and tables
db.create_all()


def group_id_generator():
    """
    Generate unique group id
    :return:
    """
    return str(uuid.uuid1())


def error_response(err_msg):
    """
    Accept error message data
    :param err_msg: error message from the custom exception
    :return: list: json dict with error message
    """
    return flask.jsonify([{'error_message': err_msg}])


def create_factual_api():
    """
    Initialize Factual API object and returns it.
    :return: object: fatual API object
    """
    # initialize factual API
    factual = Factual(settings.FACTUAL_API_KEY, settings.FACTUAL_API_SECRET)
    factual_table_data = factual.table(constants.API_ENDPOINT)
    return factual_table_data


class FindShopsResource(Resource):
    def get(self):
        """
        Get location and type of the cuisine,
        Return shops detail based on geo coordinate points using
        GOOGLE MAP API and Factual API.
        :return: list: list of dictionary about cuisine details order by distance in ascending
        """
        try:
            location = request.values.get("location")
            type_val = request.values.get("type")

            if not location or not type_val:
                return {'result': {'error': 'parameters location or type is missing'}}
            else:
                # initialise factual object
                factual_table_data = create_factual_api()
                # find geo points
                obj_geo = GeoPoints(location)
                lat, lng = obj_geo.find_geo_points()
                # filter based on geo points and type of the cuisine type with a distance in ascending order.
                data = factual_table_data.geo(circle(lat, lng, constants.GEO_CIRCLE_DISTANCE_METER)) \
                    .sort_asc('$distance').filters({'cuisine': type_val}).limit(constants.RESULT_LIMIT).data()
                return flask.jsonify(data)
        except LocationEmptyError as e:
            logger.exception("LocationEmptyError error occurred: %s", e)
            return error_response(e)
        except NoResultFound as e:
            logger.exception("NoResultFound error occurred: %s", e)
            return error_response(e)
        except Exception as e:
            logger.exception("Error occurred in FindShopsResource class, get method: %s", e)
            error_message = "something went wrong, please contact support team"
            return error_response(error_message)


class RecommendationResource(Resource):
    def post(self):
        """
        get location and user inputs details (likes, dislikes, requirements),
        process recommendation logic, uses geo coordinate points by
        GOOGLE MAP API and include, exclude features in Factual API
        :return: list: list of dict about recommendation details
        """
        try:
            location = request.values.get("location")
            input_data = flask.json.loads(request.data)
            # find least satisfying recommendation
            obj_recomm = Recommendation(input_data)
            obj_recomm.validate()
            group_id = group_id_generator()
            # create records in database
            for ele in input_data:
                group_member = RecommendationLogging(ele.get('name', ''),
                                                     ele.get('title', ''),
                                                     ','.join(ele.get('likes', [])),
                                                     ','.join(ele.get('dislikes', [])),
                                                     ele.get('requirements', ''),
                                                     group_id,
                                                     )
                db.session.add(group_member)
                db.session.commit()

            result_likes, result_dislikes, result_requirement = obj_recomm.process_data()
            # find geo points
            obj_geo = GeoPoints(location)
            lat, lng = obj_geo.find_geo_points()
            # find shops based on recommendation logic
            factual_table_data = create_factual_api()
            data = factual_table_data.geo(circle(lat, lng, constants.GEO_CIRCLE_DISTANCE_METER)).sort_asc('$distance') \
                .filters({'cuisine': {'$includes_any': result_likes, '$excludes_any': result_dislikes}}) \
                .limit(constants.RESULT_LIMIT).data()
            return flask.jsonify(data)
        except InputDataError as ex:
            logger.exception("InputDataError error occurred: %s", ex)
            return error_response(ex)
        except Exception as e:
            logger.exception("Error occurred in RecommendationResource class, post method: %s", e)
            error_message = "something went wrong, please contact support team"
            return error_response(error_message)


api.add_resource(FindShopsResource, '/find')
api.add_resource(RecommendationResource, '/recommend')

if __name__ == "__main__":
    app.run(debug=True)
