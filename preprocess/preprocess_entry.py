# File entry.py

import os
from config import *
from model.para_data import ParaDataReader
from preprocess.basic_slicer import BasicSlicer
from preprocess.basic_aligner import BasicAligner


def main():
    """
    Preprocess entry method : read data -> slice -> align -> store
    :return: None
    """
    outfile = open(os.path.join(ALIGNED_SLICE_DIR, RESULT_FILE), 'w')

    reader = ParaDataReader()
    slicer = BasicSlicer()
    aligner = BasicAligner()

    for (i, filename) in enumerate(os.listdir(RAW_DATA_DIR)):
        # get file full path
        filepath = os.path.join(RAW_DATA_DIR, filename)

        # read raw data
        data_instance = reader.read_data(filepath)

        # slice data
        slices = slicer.slice_para_data(data_instance)

        # align slices
        aligned_slices = aligner.align_slices(data_instance, slices)

        # store
        for aligned_slice_instance in aligned_slices:
            outfile.write(str(aligned_slice_instance))
            outfile.write('\n')

        # print
        print('[%s] Finish preprocessing %s ...' % (i, filename))

    outfile.close()


# self test
if __name__ == '__main__':

    import time
    start_time = time.clock()
    main()
    end_time = time.clock()
    print('[Time usage : %.6s s]' % (end_time - start_time))
