# File searcher.py


class Searcher:

    def __init__(self, manager):
        self.manager = manager

    def search_single_points(self, points):
        raise NotImplementedError

    def search_multi_points(self, points_array):
        raise NotImplementedError