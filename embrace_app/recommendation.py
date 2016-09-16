from base_exception import InputDataError
import copy


class Recommendation:
    """
    Based on Cuisine likes,dislikes and requirement inputs, it process the business logic and respond back
    with recommendations details
    """

    def __init__(self, input):
        """
        initialize the data
        :param input: list of dictionary which contains valid input data.
        """
        self.input_data = input

    def validate(self):
        """
        check the input data and raise an exception if data is invalid
        :return:
        """
        try:
            if not self.input_data:
                raise InputDataError
            else:
                for ele in self.input_data:
                    # check all the keys are present in the dict.
                    map(lambda x: ele[x], ['name', 'title', 'likes', 'dislikes'])
        except KeyError as ex:
            raise InputDataError

    def recursive_operation(self, input_list):
        """
        loop through to get least satisfaction result from the group.
        :param input_list: contains likes, dislikes, requirement list of set.
        :return:
        """
        result = None
        while True:
            # get intersection of all the list
            result = set.intersection(*input_list)
            if not result:
                # eliminate one person from the list
                input_list = input_list[0:-1]
                if len(input_list) <= 1:
                    result = set.intersection(*input_list)
                    break
            else:
                break
        return list(result)

    def process_data(self):
        """
        process input data and return the recommendation details
        :return:
        """
        temp_data = copy.deepcopy(self.input_data)
        likes_list = []
        dislikes_list = []
        requirement_list = []

        for row in temp_data:
            likes_list.append(set(row['likes']))
            dislikes_list.append(set(row['dislikes']))
            if row.get('requirements', []):
                requirement_list.append(set([row['requirements']]))

        # find intersection of all the data.
        result_likes = self.recursive_operation(likes_list)
        result_dislikes = self.recursive_operation(dislikes_list)
        result_requirement = self.recursive_operation(requirement_list)
        return result_likes, result_dislikes, result_requirement
