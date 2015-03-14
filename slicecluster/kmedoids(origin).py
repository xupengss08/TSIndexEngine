"""
Another clusting method , k-medoids.
See more : http://en.wikipedia.org/wiki/K-medoids
The most common realisation of k-medoid clustering is the Partitioning Around Medoids (PAM) algorithm and is as follows:[2]
1. Initialize: randomly select k of the n data points as the medoids
2. Associate each data point to the closest medoid. ("closest" here is defined using any valid distance metric, most commonly Euclidean distance, Manhattan distance or Minkowski distance)
3. For each medoid m
     For each non-medoid data point o
         Swap m and o and compute the total cost of the configuration
4. Select the configuration with the lowest cost.
5. repeat steps 2 to 4 until there is no change in the medoid.
"""

import random
import util.util as util

distances_cache = {}

def totalcost(blogwords, costf, medoids_idx) :
    size = len(blogwords)
    total_cost = 0.0
    medoids = {}
    for idx in medoids_idx :
        medoids[idx] = []
    for i in range(size) :
        choice = None
        min_cost = 2 ** 20
        for m in medoids :
            tmp = distances_cache.get((m,i),None)
            if tmp == None :
                tmp = costf(blogwords[m],blogwords[i])
                distances_cache[(m,i)] = tmp
            if tmp < min_cost :
                choice = m
                min_cost = tmp
        medoids[choice].append(i)
        total_cost += min_cost
        print(i, min_cost)
    return total_cost, medoids
    

def kmedoids(blogwords, k) :
    size = len(blogwords)
    medoids_idx = random.sample([i for i in range(size)], k)
    pre_cost, medoids = totalcost(blogwords,slice_distance,medoids_idx)
    print(pre_cost)
    current_cost = 2 ** 20
    best_choice = []
    best_res = {}
    iter_count = 0
    while True :
        for m in medoids :
            for item in medoids[m] :
                if item != m :
                    idx = medoids_idx.index(m)
                    swap_temp = medoids_idx[idx]
                    medoids_idx[idx] = item
                    tmp,medoids_ = totalcost(blogwords,slice_distance,medoids_idx)
                    #print tmp,'-------->',medoids_.keys()
                    if tmp < current_cost :
                        best_choice = list(medoids_idx)
                        best_res = dict(medoids_)
                        current_cost = tmp
                    medoids_idx[idx] = swap_temp
        iter_count += 1
        print(current_cost,iter_count)
        if best_choice == medoids_idx : break
        if current_cost <= pre_cost :
            pre_cost = current_cost
            medoids = best_res
            medoids_idx = best_choice

    return current_cost, best_choice, best_res




def slice_distance(slice1, slice2):
    """
    Calculate distance between two slices.
    """
    return util.getslideeuclideandis(slice1.points, slice2.points)

def print_match(best_medoids, blognames) :
    for medoid in best_medoids :
        print(blognames[medoid],'----->')
        for m in best_medoids[medoid] :
            print('(',m,blognames[m],')')
        print()
        print('---------' * 20)

