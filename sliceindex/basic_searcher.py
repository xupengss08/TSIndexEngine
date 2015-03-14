# File basic_searcher.py


from sliceindex.searcher import Searcher


class BasicSearcher(Searcher):

    def __init__(self, manager, pos_interval=3):
        Searcher.__init__(self, manager)
        self.pos_interval = 3

    def search_single_points(self, points):
        index_i, index_item = self.manager.search_data_points(points)
        return index_i, index_item.index_map

    def search_multi_points(self, points_array):
        """ Override super abstract method. """
        assert points_array

        # This list used for containing relative cluster number points_array.
        # For example, [1,2,3] means the the first slice match the 1st cluster, and so on.
        tag_list = []
        # Map for each tag and its relative index_map
        single_results = {}

        # Fill tag_list and single_results.
        for points in points_array:
            index_i, index_map = self.search_single_points(points)
            if index_i not in tag_list:
                single_results[index_i] = index_map
            tag_list.append(index_i)
        print('Parser tags : %s' % tag_list)

        # Extract equipments that appear in all tags.
        size = len(single_results.keys())
        match_equips = set()
        count_map = {}
        for single_result in single_results.values():
            for equip_name in single_result.keys():
                if equip_name not in count_map:
                    count_map[equip_name] = 0
                count_map[equip_name] += 1
        for equip_name in count_map.keys():
            if count_map[equip_name] == size:
                match_equips.add(equip_name)
        print('Mathced equips : %s' % str(match_equips))

        # Union result for each equipment
        for equip_name in match_equips:
            # Union positions of each tag for this equipment.
            pair_list = []
            for (index_i, single_result) in single_results.items():
                pos_list = single_result[equip_name]
                for pos in pos_list:
                    pair_list.append((pos, index_i))
            pair_list.sort(key=lambda pair: pair[0][0])
            # print('%s, %s' % (equip_name, str(pair_list)))

            # Find result within the pos_interval limit.
            list_start = 0
            while list_start < len(pair_list):
                if pair_list[list_start][1] != tag_list[0]:
                    list_start += 1
                    continue
                last_match_index = list_start
                list_index = list_start + 1
                tag_index = 1
                while list_index < len(pair_list) and tag_index < len(tag_list):
                    if pair_list[list_index][0][0] - pair_list[last_match_index][0][0] > self.pos_interval:
                        break
                    if pair_list[list_index][1] != tag_list[tag_index]:
                        list_index += 1
                        continue
                    else:
                        last_match_index = list_index
                        list_index += 1
                        tag_index += 1
                        continue
                if tag_index == len(tag_list):
                    for i in range(list_start, list_index):
                        if pair_list[i][1] != tag_list[0]:
                            break
                    print('[ %s ]' % equip_name, end=' ')
                    for i in range(i - 1, list_index):
                        print(pair_list[i], end=' ')
                    print()
                    list_start = list_index
                else:
                    list_start += 1


def main():
    searcher = BasicSearcher()


# self test
if __name__ == '__main__':
    main()