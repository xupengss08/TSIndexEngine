# File aligned_slice.py


class AlignedSlice:
    """
    Class to store single slice info after alignment, including:
        1) The equipment name slice belongs to
        2) The order of slice ( starts from 0 )
        3) Slice start point index
        4) Slice end point index
        5) Slice points after alignment
    """

    def __init__(self, equip_name, order, start_index, end_index):
        self.equip_name = equip_name
        self.order = order
        self.start_index = start_index
        self.end_index = end_index
        self.points = []

    def __len__(self):
        return len(self.points)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.equip_name,
                                       self.order,
                                       self.start_index,
                                       self.end_index,
                                       str(self.points)[1:-1])

    def briefstr(self):
        """
        Brief string of AlignedSlice instance.
        :return:
        """
        return '%s,%s,%s,%s' % (self.equip_name,
                                self.order,
                                self.start_index,
                                self.end_index)


class AlignedSliceReader:
    """ AlignedSlice reader : read AlignedSlice instance from string """

    def read_aligned_slice(self, slicestring):
        """
        Read aligned slice method.
        :param slicestring: the string contains aligned slice info
        :return: AlignedSlice instance
        """
        assert slicestring

        groups = slicestring.rstrip().split(',')
        slice_instance = AlignedSlice(groups[0], int(groups[1]), int(groups[2]), int(groups[3]))
        points = groups[4:]
        for point in points:
            slice_instance.points.append(float(point))
        return slice_instance


def main():
    reader = AlignedSliceReader()
    slice_instance = reader.read_aligned_slice(
        '11BC53130028, 1, 30, 53, 25.0, 28.7, 32.1, 35.1, 36.8, 36.5, 36.2, 36.9, 41.4, 45.7, 49.5, 51.0,'
        ' 51.0, 51.0, 51.3, 52.3, 53.2, 54.3, 55.8, 57.4, 59.0, 59.3, 59.6, 59.9, 60.0, 60.0, 60.0,'
        ' 60.0, 60.0, 60.0, 58.9, 56.4, 53.9, 51.8, 51.2, 50.6, 49.9, 49.0, 48.1, 47.1, 48.7, 50.8,'
        ' 53.0, 54.2, 55.5, 56.7, 57.5, 58.1, 58.7, 56.8, 53.3, 53.1, 55.0, 56.8, 56.7, 53.7, 52.2, '
        '52.8, 53.5, 54.0, 54.0, 54.0, 54.0, 53.8, 52.8, 51.9, 51.0, 50.1, 49.2, 48.2, 47.3')
    print(slice_instance)


# self test
if __name__ == '__main__':
    main()