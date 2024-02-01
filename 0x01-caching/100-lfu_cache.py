#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching"""

    def __init__(self):
        """overload"""
        super().__init__()
        self.__tracking = []

    def index(self, key):
        """returns"""
        i = 0
        for svd_key, cnt in self.__tracking:
            if svd_key == key:
                return i
            i += 1
        return None

    def ht(self, key):
        """update ht"""
        index = self.index(key)
        if index is None:
            return
        _key, cnt = self.__tracking[index]
        self.__tracking[index] = (_key, cnt + 1)

    def pop(self):
        """assign to the dictionary self.cache_data"""
        from functools import reduce
        mth = reduce(lambda x, y: x if x[1] <= y[1] else y,
                       self.__tracking)
        _key, cnt = self.__tracking.pop(self.__tracking.index(mth))
        return _key

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

        if len(self.cache_data) <= self.MAX_ITEMS:
            if self.index(key) is None:
                self.__tracking.append((key, 0))
            else:
                self.ht(key)
            return

        if self.index(key) is None:
            pop_key = self.pop()
            self.cache_data.pop(pop_key)
            print('DISCARD: {}'.format(pop_key))
            self.__tracking.append((key, 0))
        return

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        self.ht(key)
        return self.cache_data.get(key, None)
