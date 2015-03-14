# File basicdivider.py


import os
from config import *
from slicecluster.divider import BucketDivider


class IntervalBucketDivider(BucketDivider):
    """
    An implement of basic bucket divider : user define an interval, we'll create bucket with same interval,
    slice should fall into the certain bucket according its point list length.
    """

    def __init__(self, slices, width):
        BucketDivider.__init__(self, slices)
        self.width = width

    def divide_slices(self):
        """ Override BucketDivider abstract method. """

        # calculate max and min slice length
        minlen = MAX_NUMBER
        maxlen = 0
        for slice_instance in self.slices:
            if minlen > len(slice_instance):
                minlen = len(slice_instance)
            if len(slice_instance) > maxlen:
                maxlen = len(slice_instance)
        print(maxlen, minlen)

        # calculate bucket count and store
        bucketcount = int((maxlen - minlen) / self.width) + 1
        self.store_mapping_info(bucketcount, minlen)

        # put each slice into its corresponding bucket
        buckets = []
        for i in range(bucketcount):
            buckets.append([])
        for slice_instance in self.slices:
            bucketindex = int((len(slice_instance) - minlen) / self.width)
            buckets[bucketindex].append(slice_instance)
        for (i, bucket) in enumerate(buckets):
            print(i, len(bucket))
        return buckets

    def store_mapping_info(self, bucketcount, minlen):
        """ Override BucketDivider abstract method. """
        with open(os.path.join(CLUSTER_RESULT_DIR, BUCKET_FILE), 'w') as file:
            for i in range(bucketcount):
                file.write('%s,%s,%s' % (i,
                                         minlen + i * self.width,
                                         minlen + (i + 1) * self.width))
                file.write('\n')


