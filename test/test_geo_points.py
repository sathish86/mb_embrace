import pytest
from embrace_app.geo_points import GeoPoints
from embrace_app.base_exception import LocationEmptyError, NoResultFound


class TestGeoPoints(object):
    @pytest.fixture(autouse=True)
    def create_instance(self, request):
        self.obj = GeoPoints("")

        def teardown():
            self.obj = None

        request.addfinalizer(teardown)

    def test_validator__empty(self, create_instance):
        """
        Check validator method.
        """
        self.obj.location = ""
        with pytest.raises(LocationEmptyError) as excinfo:
            self.obj.validator()

    def test_validator__special_char(self, create_instance):
        """
        Check validator method.
        """
        self.obj.location = "Bella $%# Vista"
        with pytest.raises(LocationEmptyError) as excinfo:
            self.obj.validator()

    def test_validator__digits(self, create_instance):
        """
        Check validator method.
        """
        self.obj.location = "Bella23Vista"
        with pytest.raises(LocationEmptyError) as excinfo:
            self.obj.validator()

    def test_validator__correct_value(self, create_instance):
        """
        Check validator method.
        """
        self.obj.location = "Bella Vista"
        assert self.obj.validator() is None

    def test_find_geo_points__correct_location(self, create_instance):
        """
        Check find_geo method
        :return: None
        """
        self.obj.location = "woolloomooloo"
        lat, lng = self.obj.find_geo_points()
        assert lat is not None and lng is not None

    def test_find_geo_points__incorrect_location(self, create_instance):
        """
        Check find_geo method
        :return: None
        """
        self.obj.location = "woasdfasdfasdfolloomooloo"
        with pytest.raises(NoResultFound) as excinfo:
            self.obj.find_geo_points()

