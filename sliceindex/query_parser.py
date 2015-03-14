# File query_parse.py

"""

"""


from model.para_data import ParaDataReader
from preprocess.basic_slicer import BasicSlicer
from preprocess.basic_aligner import BasicAligner


class QueryParser:
    """
    This class accepts equipment raw data and do slice and align work.
    """

    def __init__(self):
        self.reader = ParaDataReader()
        self.slicer = BasicSlicer()
        self.aligner = BasicAligner()

    def parse_query_file(self, file_path):
        """
        Read query file and do slice and align work.
        :param file_path: query file full path
        :return: aligned slice instance list
        """
        # read raw data
        data_instance = self.reader.read_data(file_path)

        # slice data
        slices = self.slicer.slice_para_data(data_instance)

        # align slices
        aligned_slices = self.aligner.align_slices(data_instance, slices)

        return aligned_slices


def main():
    import os
    import config

    query_parser = QueryParser()
    file_path = os.path.join(config.QUERY_DATA_DIR, 'query.dat')
    aligned_slices = query_parser.parse_query_file(file_path)

    for aligned_slice_instance in aligned_slices:
        print(aligned_slice_instance)


# self test
if __name__ == '__main__':
    main()