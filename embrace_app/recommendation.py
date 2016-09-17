from base_exception import InputDataError
import copy


class Recommendation:
    """
    Based on input details about cuisine likes,dislikes and requirement, this class process the business logic
    to find recommendations which tries to satisfies most of the group members.
    """

    def __init__(self, data):
        """
        initialize the data
        :param data: list of dictionary which has user input data.
        """
        self.input_data = data

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

    def find_common_interest(self, input_list):
        """
        loop through the data to get (most to least) satisfaction result from the group members.
        :param input_list: contains any of this likes, dislikes, requirement list of set.
        :return: list : list of elements
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
        process input data and return the recommendation details by finding out (most to least) common from the group
        members
        :return: list: likes, dislikes, requirement elements
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
        result_likes = self.find_common_interest(likes_list)
        result_dislikes = self.find_common_interest(dislikes_list)
        result_requirement = self.find_common_interest(requirement_list)
        return result_likes, result_dislikes, result_requirement
