# File basic_slicer.py

"""
A basic implement of Slicer.

Args:
    slice_interval: time interval between two slices (ms)
    min_slice_count: minimum point count in a slice

Algorithm:
    Each slice follows the following two rules:
    1) latter slice start time - former slice end time > slice_interval
    2) end_index - start_index >= min_slice_count
"""


from preprocess.slicer import Slicer


class BasicSlicer(Slicer):
    """ A basic implement of Slicer """

    def __init__(self, slice_interval=7200000, min_slice_count=10):
        self.slice_interval = slice_interval
        self.min_slice_count = min_slice_count

    def slice_para_data(self, para_data):
        """ Override Slicer abstract method """
        points = para_data.points
        assert len(points) > 0

        slice_start_index = 0
        slices = []
        for i in range(len(points) - 1):
            if i < slice_start_index:
                continue
            current_point = points[i]
            next_point = points[i + 1]
            if next_point[0] - current_point[0] > self.slice_interval:
                if i - slice_start_index + 1 >= self.min_slice_count:
                    slices.append((slice_start_index, i))
                slice_start_index = i + 1

        if len(points) - slice_start_index >= self.min_slice_count:
            slices.append((slice_start_index, len(points) - 1))
        return slices

    # def __str__(self):
    #     result = ''
    #     for slice in self.slices:
    #         result += str(slice) + '\n'
    #     return result


def main():
    from model.para_data import ParaData, ParaDataReader
    reader = ParaDataReader()
    data_instance = reader.read_data(r'..\resources\raw_data\11BC53130028.csv')
    print(data_instance)

    slicer = BasicSlicer()
    slices = slicer.slice_para_data(data_instance)
    print('Slices : %s' % str(slices))


# self test
if __name__ == '__main__':
    main()
