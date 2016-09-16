import pytest
from embrace_app.recommendation import Recommendation
from embrace_app.base_exception import InputDataError


class TestGeoPoints(object):
    @pytest.fixture(autouse=True)
    def create_instance(self, request):
        self.obj = Recommendation([])

        def teardown():
            self.obj = None

        request.addfinalizer(teardown)

    def test_validator__empty(self, create_instance):
        """
        Check validator method.
        """
        self.obj.input_data = []
        with pytest.raises(InputDataError) as excinfo:
            self.obj.validate()

    def test_validator__invalid_data(self, create_instance):
        """
        Check validator method.
        """
        self.obj.input_data = [
            {
                "name": "Bob",
                "title": "executive",
                "likes": [
                    "indian",
                    "chinese",
                    "malaysian"
                ],
                "dislike": ["Australian"],
                "requirements": "gluten free"
            }
        ]
        with pytest.raises(InputDataError) as excinfo:
            self.obj.validate()

    def test_validator__valid_input(self, create_instance):
        """
        Check validator method.
        """
        self.obj.input_data = [
            {
                "name": "Bob",
                "title": "executive",
                "likes": [
                    "indian",
                    "chinese",
                    "malaysian"
                ],
                "dislikes": ["Australian"],
                "requirements": "gluten free"
            },
            {
                "name": "Jose",
                "title": "developer",
                "likes": [
                    "indian",
                    "chinese"
                ],
                "dislikes": ["thai"]
            },
            {
                "name": "Aloysia",
                "title": "evangelist",
                "likes": [
                    "chinese"
                ],
                "dislikes": ["Australian"],
                "requirements": "gluten free"
            }
        ]
        like, dislike, requirement = self.obj.process_data()
        assert like == ['chinese']
        assert dislike == ['Australian']
        assert requirement == ['gluten free']
