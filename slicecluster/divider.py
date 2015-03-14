# File divider.py


class BucketDivider:
    """
    As the whole number of slices is too large for direct clustering, and also provide a way for
    later map-reduce extension, we try to create several buckets and divide the whole slices into
    each bucket before clustering.
    This is a super class of bucket divider, it accepts a list of slices and comes out a list of
    buckets, each bucket contains a list of slices. The union of all buckets is the list of slices.
    """
    def __init__(self, slices):
        self.slices = slices

    def divide_slices(self):
        """
        This method do the main dividing function.
        :return: bucket list
        """
        raise NotImplementedError

    def store_mapping_info(self):
        """
        This method store the bucket mapping info.
        :return: None
        """
        raise  NotImplementedError

