import constants
import requests
import re
from base_exception import LocationEmptyError, NoResultFound


class GeoPoints:
    """
    Find geo points of a location using Google Map API
    """

    def __init__(self, location):
        self.location = location

    def validator(self):
        """
        validate location value with these condition empty, special characters or digits
        :return: None
        """
        if (not self.location) or (not re.findall(r'(^[a-zA-Z ]*$)', self.location)):
            raise LocationEmptyError(self.location)

    def find_geo_points(self):
        """
        find the goe points of a location using Google map API.
        Note: Google MAP API has 2500 request limit per day.

        :param location: string value
        :return: list: geo points of a location
        """
        self.validator()
        payload = {'address': self.location+constants.COUNTRY, 'sensor': 'false'}
        response = requests.get(constants.GOOGLE_MAP_API, params=payload).json()
        try:
            if response.get("status") == "ZERO_RESULTS":
                raise NoResultFound(self.location)

            if response.get("results", None):
                # read first element from the response
                location = response.get("results")[0].get("geometry").get('location')
                return location['lat'], location['lng']
        except AttributeError as e:
            raise NoResultFound(self.location)



