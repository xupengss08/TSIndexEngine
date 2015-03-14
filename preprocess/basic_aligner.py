# File basic_aligner.py

"""
A basic implement of Aligner.

Args:
    align_interval: the time interval that we align data points, that is to say,
    after alignment, the time series should be (d1, d2, d3, ...) with relatively
    timestamp (t, t+i, t+2i, ...) i = align_interval.

Algorithm:

"""

from preprocess.aligner import Aligner
from model.aligned_slice import AlignedSlice
from util.util import binarysearch, getlinearvalue


class BasicAligner(Aligner):
    """ A basic implement of Aligner """

    def __init__(self, align_interval=600000):
        self.align_interval = align_interval

    def align_slices(self, para_data, slices):
        """ Override Aligner abstract method """
        assert para_data
        assert para_data.points
        assert slices

        # extract point list
        points = para_data.points
        aligned_slices = []

        # align each slice
        for (order, slice_instance) in enumerate(slices):
            slice_points = points[slice_instance[0]: slice_instance[1] + 1]
            # create AlignedSlice instance with result of single slice data
            aligned_slice_instance = AlignedSlice(para_data.equip_name,
                                                  order,
                                                  slice_instance[0],
                                                  slice_instance[1])
            aligned_slice_instance.points = self.align_signal_slice(slice_points, self.align_interval)
            aligned_slices.append(aligned_slice_instance)
        return aligned_slices

    def align_signal_slice(self, slice_points, align_interval):
        """
        Align data of given interval for points in a slice.
        :param slice_points: point list of a slice
        :param align_interval: align interval
        :return: aligned data
        """
        assert slice_points
        assert len(slice_points)

        # extract slice time list and slice value list
        result = []
        slice_times = [point[0] for point in slice_points]
        slice_values = [point[1] for point in slice_points]

        # calculate aligned value count
        count = int((slice_times[len(slice_points) - 1] - slice_times[0]) / align_interval) + 1
        for i in range(count):
            # search the insertion time for each value that should be aligned
            insertion_time = slice_times[0] + i * align_interval
            align_index = binarysearch(slice_times, insertion_time)
            if align_index >= 0:
                result.append(slice_values[align_index])
            else:
                align_index = -align_index - 1
                if align_index < len(slice_times):
                    result.append(getlinearvalue(slice_times[align_index - 1], slice_values[align_index - 1],
                                                 slice_times[align_index], slice_values[align_index],
                                                 insertion_time))
        return result


def main():
    from model.para_data import ParaData, ParaDataReader
    from preprocess.basic_slicer import BasicSlicer

    reader = ParaDataReader()
    data_instance = reader.read_data(r'..\resources\raw_data\11BC53130028.csv')
    print(data_instance)

    slicer = BasicSlicer()
    slices = slicer.slice_para_data(data_instance)
    print('Slices : %s' % str(slices))

    aligner = BasicAligner()
    aligned_slices = aligner.align_slices(data_instance, slices)
    print('Aligned Slices:')
    for (i, aligned_slice_instance) in enumerate(aligned_slices):
        print('%s) %s' % (i, str(aligned_slice_instance)))


# self test
if __name__ == '__main__':
    main()