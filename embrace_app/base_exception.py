class LocationEmptyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        err_msg = "Location value is empty or not a valid value: %s" % self.msg
        return err_msg


class NoResultFound(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        err_msg = "No result found for this location: %s" % self.msg
        return err_msg


class InputDataError(Exception):
    def __init__(self):
        input_str = """[    {
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
                            """
        self.msg = input_str

    def __str__(self):
        err_msg = "Input data is not valid, Example input data: %s" % self.msg
        return err_msg