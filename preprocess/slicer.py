# File slicer.py


class Slicer:
    """ Class that accept a ParaData instance and slice the raw data """

    def slice_para_data(self, para_data):
        """
        Split data points into several slices, each slice is a (start_index, end_index) pair.
        :param para_data: input ParaData instance, contains data point list.
        :return: slice boundary pair (start_index, end_index) list.
        """
        raise NotImplementedError