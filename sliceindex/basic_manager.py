# File basic_manager.py


import util.util as Util
from config import *
from sliceindex.manager import IndexManager


class ListIndexManager(IndexManager):
    """
    Index manager of basic list index items construct :
        use list to put all index items
    """
    def __init__(self):
        # InvertedItem instance list
        self.index_items = []
        self.data_map = {}
        # self.slices = {}

    def add_raw_data(self, para_datas):
        """ Override super class abstract method. """
        for para_data in para_datas:
            self.data_map[para_data.equip_name] = para_data.points

    # def addslices(self, slices):
    #     """
    #     Add all slices to the manager.
    #     :param slices:
    #     :return:
    #     """
    #     for slice in slices:
    #         if slice.equipname not in self.slices:
    #             self.slices[slice.equipname] = {}
    #         equipmap = self.slices[slice.equipname]
    #         equipmap[slice.order] = slice.points

    def add_index_item(self, index_item):
        """ Override super class abstract method. """
        self.index_items.append(index_item)

    def search_data_points(self, data_points):
        """ Override super class abstract method. """
        min_dis = MAX_NUMBER
        best_index_item = None
        best_index_i = -1
        for (i, index_item) in enumerate(self.index_items):
            tmp_dis = Util.getslideeuclideandis(index_item.get_core_points(),
                                                data_points)
            if tmp_dis < min_dis:
                min_dis = tmp_dis
                best_index_i = i
                best_index_item = index_item
        return best_index_i, best_index_item

    # def findrawpoints(self, equipname, startindex, endindex):
    #     """
    #     Find the raw data points of certain equipname and certain start & end index.
    #     :param equipname:
    #     :param startindex:
    #     :param endindex:
    #     :return: raw data points
    #     """
    #     points = self.datas[equipname]
    #     if points:
    #         try:
    #             return points[startindex: endindex + 1]
    #         except IndexError:
    #             return []
    #     return []
    #
    # def findslicepoints(self, equipname, sliceorder):
    #     """
    #     Find the slice points of certain equipname and slice order
    #     :param equipname:
    #     :param sliceorder:
    #     :return:
    #     """
    #     equipmap = self.slices[equipname]
    #     if equipmap:
    #         return equipmap[sliceorder]
    #     return []

    def __str__(self):
        disstring = 'ListIndexManager : \n'
        disstring += 'Core Slice count : %s\n' % len(self.index_items)
        for (i, item) in enumerate(self.index_items):
            disstring += str(i) + ') ' + str(item) + '\n'
        return disstring