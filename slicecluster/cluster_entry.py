# File cluster_entry.py


import os
from config import *
from model.aligned_slice import AlignedSliceReader
from slicecluster.kmediods_cluster import KMediodsCluster


def main():
    # remove old cluster result files
    clear_old_indexes()

    # load slices
    slices = import_aligned_result()

    # divide slices into server buckets
    # divider = basicdivider.IntervalBucketDivider(slices, 5)
    # divider.divide_slices()

    # run clustering methods to get the best clusters and relative mediods
    best_mediods, best_clusters = get_best_cluster(slices)

    # store result
    store_index_files(best_mediods, best_clusters, slices)


def import_aligned_result():
    """
    Import slices from aligned slice data file.
    """
    slices = []
    reader = AlignedSliceReader()
    file = open(os.path.join(ALIGNED_SLICE_DIR, RESULT_FILE))
    for line in file.readlines():
        slice_instance = reader.read_aligned_slice(line)
        # print(slice)
        slices.append(slice_instance)
    return slices


def clear_old_indexes():
    """
    Clear old index files.
    """
    for f in os.listdir(CLUSTER_RESULT_DIR):
        if f.endswith('.idx'):
            os.remove(os.path.join(CLUSTER_RESULT_DIR, f))
            

def get_best_cluster(slices):
    # create cluster
    cluster_instance = KMediodsCluster(slices)
    best_score = -1
    best_mediods = []
    best_clusters = {}

    # clustering min & max k
    kmin = 2
    kmax = int(len(slices) ** 0.5)
    # try to clustering certain times of each k
    times = 1

    # do k-mediods clustering for different k
    for k in range(kmin, kmax + 1):
        print('========================= k = %s =========================' % k)
        for i in range(times):
            # display clustering result
            cost, score, mediods, clusters = cluster_instance.cluster_slices(k)
            print('Time:%s,  Cost:%.4f,  Score:%.4f,  Mediods:%s' % (i, cost, score, mediods))
            if len(clusters) < 50:
                print('         Clusters:%s' % clusters)

            # change best result
            if score > best_score:
                best_score = score
                best_mediods = mediods
                best_clusters = clusters

    # display best clustering result
    print('========================= best cluster =========================')
    print('Score:%.4f,  Mediods:%s' % (best_score, best_mediods))
    print('Clusters:%s' % best_clusters)
    return best_mediods, best_clusters


def store_index_files(best_mediods, best_clusters, slices):
    for i in range(len(best_mediods)):
        # create result file name
        filename = 'cluster_%s.idx' % i
        mediod_key = best_mediods[i]
        cluster = best_clusters[mediod_key]
        with open(os.path.join(CLUSTER_RESULT_DIR, filename), 'w') as file:
            # store mediod slice info
            mediod_slice = slices[mediod_key]
            file.write(mediod_slice.briefstr())
            file.write('\n\n')
            # store cluster slices info
            for slice_index in cluster:
                slice_instance = slices[slice_index]
                file.write(slice_instance.briefstr())
                file.write('\n')


# self test
if __name__ == '__main__':
    main()