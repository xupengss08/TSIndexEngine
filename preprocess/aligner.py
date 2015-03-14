# File aligner.py


class Aligner:
    """ Class that do data alignment for each slice """

    def align_slices(self, para_data, slices):
        """
        Align all slices of an equipment
        :param para_data: ParaData instance
        :param slices: slice list
        :return: AlignedSlice instance list
        """
        raise NotImplementedError