# File para_data.py

import os


class ParaData:
    """ Class for supporting data of certain equipment with certain parameter. """

    def __init__(self):
        self.equip_name = ''     # equipment name
        self.points = []        # equipment raw data point list

    def add_point(self, time, value):
        """
        Add a (time, value) pair data point.
        :param time: data point time (ms)
        :param value: data point value
        :return: None
        """
        self.points.append((time, value))

    def __str__(self):
        return 'EquipName : %s\nPoints : %s' % (self.equip_name, str(self.points))


class ParaDataReader:
    """ ParaData reader: read raw data file and construct ParaData instance. """

    def read_data(self, filepath):
        """
        Read data method
        :param filename: para data file name ( with .csv postfix )
        :return: ParaData instance
        """
        data_instance = ParaData()
        filename = os.path.basename(filepath)
        data_instance.equip_name = filename[:filename.index('.')]          # remove postfix

        # fill instance
        for line in open(filepath).readlines():
            time, value = line.rstrip().split(',')
            data_instance.add_point(int(time), float(value))
        return data_instance


def main():
    reader = ParaDataReader()
    data_instance = reader.read_data(r'..\resources\raw_data\11BC53130028.csv')
    print(data_instance)


# self test
if __name__ == '__main__':
    main()