import constants


def filter_output(data):
    """
    remove unwanted field from the data
    :param data: list of dict
    :return: list of dict
    """
    for row_dict in data:
        [row_dict.pop(ele, None) for ele in constants.FILTER_OUTPUT_FIELDS]
    return data
