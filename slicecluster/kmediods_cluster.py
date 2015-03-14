# File kmediods_cluster.py


from slicecluster.cluster import Cluster
import util.util as util
import random


class KMediodsCluster(Cluster):

    def __init__(self, slices):
        Cluster.__init__(self, slices)
        self.distances_cache = {}

    def cluster_slices(self, k):
        """
        Main clustering method
        :param k: the slicecluster number wish to be clustered
        :return: current_cost:
                 best_score:
                 best_mediods:
                 best_clusters
        """
        # calculate distance cache
        self.cachedistances()

        size = len(self.slices)
        mediods = random.sample(list(range(size)), k)   # record mediod index
        pre_cost, clusters = self.totalcost(mediods)

        current_cost = 2 ** 32
        best_mediods = []
        best_clusters = {}
        iter_count = 0

        while True:
            for keyindex in clusters.keys():                # keyindex : mediod index
                for itemindex in clusters[keyindex]:        # itemindex : simple slice index
                    # if keyindex != itemindex, switch keyindex to itemidex,
                    # and recluster to get new total cost and new clusters.
                    if keyindex != itemindex:
                        index = mediods.index(keyindex)
                        old_mediod = mediods[index]         # record old mediod index
                        mediods[index] = itemindex
                        new_cost, new_clusters = self.totalcost(mediods)
                        # if find a better solution, record it
                        if new_cost < current_cost:
                            best_mediods = list(mediods)
                            best_clusters = dict(new_clusters)
                            current_cost = new_cost
                        mediods[index] = old_mediod
            iter_count += 1
            if best_mediods == mediods:
                break
            if current_cost <= pre_cost:
                pre_cost = current_cost
                mediods = best_mediods
                clusters = best_clusters

        # cacluate Silhouette(Clustering) performance score
        best_score = self.analyzeresult(best_clusters)

        return current_cost, best_score, best_mediods, best_clusters

    def slice_distance(self, slice1, slice2):
        """
        Calculate distance between two slices.
        """
        return util.getslideeuclideandis(slice1.points, slice2.points)

    def cachedistances(self):
        """
        Fill the distances_cache with distances of (slice index1, slice index2) pair.
        :return: None
        """
        size = len(self.slices)
        for i in range(size):
            for j in range(i, size):
                self.distances_cache[(i, j)] = self.slice_distance(
                    self.slices[i], self.slices[j])

    def totalcost(self, mediods):
        """
        Calculate the total distance cost of given mediods.
        :param mediods: mediod index list
        :return: total distance cost and slicecluster results.
        """
        size = len(self.slices)
        total_cost = 0

        # init clusters.
        clusters = {}
        for index in mediods:
            clusters[index] = []

        # add each slice into slicecluster and calculate distance
        for i in range(size):
            choice = None
            min_cost = 2 ** 32
            for m in mediods:
                tmp = self.getcacheddistance(i, m)
                if tmp < min_cost:
                    choice = m
                    min_cost = tmp
            clusters[choice].append(i)
            total_cost += min_cost
        return total_cost, clusters

    def getcacheddistance(self, index1, index2):
        """
        Get distance from cache.(As the cache pair need index1 < index2)
        :param index1:
        :param index2:
        :return: distance
        """
        return self.distances_cache[(index1, index2)] \
            if index1 <= index2\
            else self.distances_cache[(index2, index1)]

    def analyzeresult(self, clusters):
        """
        Use Silhouette(Clustering) performance score to measure the clustering
        result.
        :param clusters:
        :return: score
        """
        total_score = 0
        for cluster_key in clusters.keys():
            cluster = clusters[cluster_key]
            for item in cluster:
                # calculate Silhouette(Clustering) performance parameter m_a
                m_a = 0
                count_a = 0
                for item2 in cluster:
                    if item == item2:
                        continue
                    m_a += self.getcacheddistance(item, item2)
                    count_a += 1
                if count_a == 0:
                    m_a = 0
                else:
                    m_a /= count_a
                # calculate Silhouette(Clustering) performance parameter m_b
                m_b = 2 ** 32
                for cluster_key2 in clusters.keys():
                    if cluster_key2 == cluster_key:
                        continue
                    cluster2 = clusters[cluster_key2]
                    for item2 in cluster2:
                        dis = self.getcacheddistance(item, item2)
                        if dis < m_b:
                            m_b = dis
                # cacluate Silhouette(Clustering) performance score m_s
                m_s = (m_b - m_a) / max(m_b, m_a)
                total_score += m_s
        total_score /= len(self.slices)
        return total_score


# self test
if __name__ == '__main__':
    print()