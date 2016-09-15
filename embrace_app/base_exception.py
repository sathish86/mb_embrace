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
