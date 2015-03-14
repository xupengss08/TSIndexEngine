# File manager.py


"""
This is the Super abstract class of index manager.

Index mangager tries to read built index files in inverted document structure
and organize them in memory. When user provides a query of data points, index
manager can give out a list of search result.

Methods:
1) add_raw_data : load raw euqip para_data into the manager, for later display
2) add_index_item : load a single inverted item into the manager
3) search_data_points : search the result for input data points

"""


class IndexManager:
    """
    Index manager super class.
    """

    def add_raw_data(self, para_datas):
        """
        load raw euqip para_data into the manager, for later display
        :param para_datas:
        :return:
        """
        raise NotImplementedError

    def add_index_item(self, index_item):
        """
        load a single inverted item into the manager
        :param index_item:
        :return:
        """
        raise NotImplementedError

    def search_data_points(self, data_points):
        """
        search the result for input data points
        :param data_points:
        :return:
        """
        raise NotImplementedError
