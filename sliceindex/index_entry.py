# File entry.py

import os
from config import *
from model.para_data import ParaDataReader
from sliceindex.basic_manager import ListIndexManager
from model.inverted_item import InvertedItemReader
from sliceindex.basic_searcher import BasicSearcher
from sliceindex.query_parser import QueryParser


def main():
    # load raw data
    datas = []
    reader = ParaDataReader()
    for filename in os.listdir(RAW_DATA_DIR):
        filepath = os.path.join(RAW_DATA_DIR, filename)
        datas.append(reader.read_data(filepath))

    # load slices
    # slices = []
    # reader = AlignedSliceReader()
    # for line in open(os.path.join(ALIGNED_SLICE_DIR, RESULT_FILE)).readlines():
    #     slice = reader.read_aligned_slice(line)
    #     slices.append(slice)

    # init index manager instance
    manager = ListIndexManager()
    manager.add_raw_data(datas)
    # manager.addslices(slices)

    # points = manager.findrawpoints('11BC53130028', 3, 29)
    # print(points)
    # print(manager.findslicepoints('11BC53130028', 0))

    # init index file reader
    reader = InvertedItemReader()

    # read all index files
    for filename in os.listdir(CLUSTER_RESULT_DIR):
        if filename.endswith('.idx'):
            filepath = os.path.join(CLUSTER_RESULT_DIR, filename)
            manager.add_index_item(reader.read_inverted_item(filepath))

    # display index manager instance
    print(manager)

    searcher = BasicSearcher(manager)

    query_parser = QueryParser()
    file_path = os.path.join(QUERY_DATA_DIR, 'query.dat')
    aligned_slices = query_parser.parse_query_file(file_path)

    # points0 = [46.0, 46.3, 46.6, 46.9, 47.4, 47.9, 48.4, 48.9, 49.4, 50.0, 49.6, 49.3, 49.0, 48.3, 47.6, 47.0, 46.3, 45.6, 45.0, 45.0, 45.0, 45.0, 44.3, 43.6, 43.0, 43.0, 43.0, 43.0, 42.3, 41.6, 41.0, 41.3, 41.6, 42.0, 42.3, 42.6, 43.0, 42.3, 41.6, 41.0, 42.0, 43.0, 44.0]
    # points1 = [36.0, 37.6, 39.3, 41.0, 42.0, 43.0, 44.0, 43.6, 43.3, 43.0, 43.6, 44.3, 45.0, 44.3, 43.6, 43.0, 42.6, 42.3, 42.0, 42.4, 42.9, 43.5, 44.0, 44.5, 44.9, 44.6, 44.3, 44.0, 44.0, 44.0, 44.0]
    # points2 = [35.0, 35.6, 36.3, 37.0, 37.6, 38.3, 38.9, 39.4, 39.9, 40.4, 40.9, 41.4, 42.0, 42.3, 42.6, 43.0, 42.3, 41.6, 41.0, 40.6, 40.3, 40.0, 40.1, 40.2, 40.3, 40.4, 40.5, 40.6, 40.7, 40.8, 41.0, 41.6, 42.3, 43.0, 43.3, 43.6, 44.0, 44.0, 44.0]
    # searcher.search_single_points(points1)
    searcher.search_multi_points([aligned_slice.points for aligned_slice in aligned_slices])


# self test
if __name__ == '__main__':
    main()