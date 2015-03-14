# util.py


def binarysearch(data_list, key):
    """
    Binary Search: return the index of key in list
        1) result >= 0: means the index of key
        2) result < 0: means the insertion index of key, result = - (insertion index) - 1
        to avoid front insertion index becoming 0
    """
    low = 0
    high = len(data_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if key == data_list[mid]:          # found the key
            return mid
        elif key < data_list[mid]:         # key before the middle
            high = mid - 1
        else:                       # key after the middle
            low = mid + 1
    else:
        if data_list[mid] > key:
            return -mid - 1
        elif data_list[mid] < key:
            return -mid - 2


def getlinearvalue(begin_time, begin_value, end_time, end_value, mid_time):
    """
    Calculate the linear insertion value from (begin_time, begin_value) to (end_time, end_value)
    of given time mid_time
    :param begin_time: begin time
    :param begin_value: begin value
    :param end_time: end time
    :param end_value: end value
    :param mid_time: insertion time
    :return: mid_value
    """
    slope = (end_value - begin_value) / (end_time - begin_time)
    mid_value = begin_value + slope * (mid_time - begin_time)
    return int(mid_value * 10) / 10


def getslideeuclideandis(timeSeries, subSequence):
    """
    Calculate the minimum euclidean distance of sub-sequence sliding in the whole time series sequence.
    :param timeSeries: whole time series sequence
    :param subSequence: sub-sequence
    :return: minimum distance
    """
    assert(timeSeries)
    assert(subSequence)
    if len(timeSeries) < len(subSequence):
        return getslideeuclideandis(subSequence, timeSeries)

    mindis = 2 ** 32
    for startindex in range(len(timeSeries) - len(subSequence) + 1):
        dis = 0
        for i in range(len(subSequence)):
            dis += (timeSeries[startindex + i] - subSequence[i]) ** 2
        dis **= 0.5
        if dis < mindis:
            mindis = dis
    return mindis


# self test
if __name__ == "__main__":
    # print(binarysearch.__doc__)
    # data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(binarysearch(data_list, 0.5))
    #
    # print(getlinearvalue(1, 1, 5, 4, 2))
    print(getslideeuclideandis((1,2,3,4), (1,2,3,5)))