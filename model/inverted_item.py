# File inverted_item.py


from model.aligned_slice import AlignedSliceReader


class InvertedItem:
    """
    Basic element for inverted index, contains:
        1) Core equipname and slice order, also the mediod of cluter.
        2) Other euqipname and slice order in the same cluster, organized
        in the indexMap dictionary, the key means equipname, the value is
        a list of slice order in this equipname
    """

    def __init__(self):
        # self.equip_name = ''
        # self.slice_order = -1
        # self.slice_start_index = -1
        # self.slice_end_index = -1
        self.core_slice_item = None
        self.index_map = {}

    # def set_core_slice_item(self, equip_name, slice_order, slice_start_index, slice_end_index):
    # """
    #     Set core slice item
    #     :param equip_name: core slice equipname
    #     :param slice_order : core slice order
    #     :param slice_start_index: core slice start index
    #     :param slice_end_index: core slice end index
    #     :return:
    #     """
    #     self.equip_name = equip_name
    #     self.slice_order = slice_order
    #     self.slice_start_index = slice_start_index
    #     self.slice_end_index = slice_end_index

    def add_slice_item(self, equip_name, slice_order, slice_start_index, slice_end_index):
        """
        Add a normal cluster slice into the index map.
        :param equip_name: normal slice equipname
        :param slice_order : normal slice order
        :param slice_start_index: normal slice start index
        :param slice_end_index: normal slice end index
        :return: None
        """
        if equip_name not in self.index_map:
            self.index_map[equip_name] = []
        self.index_map[equip_name].append((slice_order, slice_start_index, slice_end_index))

    def __str__(self):
        return 'Core Slice:[ %s ]    Elements:%s' % (str(self.core_slice_item),
                                                     # self.core_slice_item.equip_name,
                                                     #             self.core_slice_item.slice_order,
                                                     #             self.core_slice_item.slice_start_index,
                                                     #             self.core_slice_item.slice_end_index,
                                                     self.index_map)

    def get_core_points(self):
        return self.core_slice_item.points


class InvertedItemReader:
    """
    Inverted item reader : read index file and construct InvertedItem instance.
    """

    def read_inverted_item(self, filepath):
        """
        Read method
        :param filepath: index file path
        :return: InvertedItem instance
        """
        file = open(filepath)
        item_instance = InvertedItem()

        reader = AlignedSliceReader()
        core_slice_item = reader.read_aligned_slice(file.readline().rstrip())
        item_instance.core_slice_item = core_slice_item

        # coresliceinfos = file.readline().rstrip().split(',')
        # item_instance.set_core_slice_item(coresliceinfos[0],
        # int(coresliceinfos[1]),
        #                                   int(coresliceinfos[2]),
        #                                   int(coresliceinfos[3]))
        file.readline()
        for line in file.readlines():
            sliceinfos = line.rstrip().split(',')
            item_instance.add_slice_item(sliceinfos[0],
                                         int(sliceinfos[1]),
                                         int(sliceinfos[2]),
                                         int(sliceinfos[3]))
        return item_instance


def main():
    reader = InvertedItemReader()
    item_instance = reader.read_inverted_item(r'..\resources\cluster_index\cluster_0.idx')
    print(item_instance)


# self test
if __name__ == '__main__':
    main()