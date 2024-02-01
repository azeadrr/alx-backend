#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache
    that inherits from BaseCaching
    """
    def __init__(self):
        """overload"""
        super().__init__()
        self.__tracking = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

        if len(self.cache_data) <= self.MAX_ITEMS:
            if key not in self.__tracking:
                self.__tracking.append(key)
            return

        if key not in self.__tracking:
            pop_key = self.__tracking.pop(0)
            self.cache_data.pop(pop_key)
            print('DISCARD: {}'.format(pop_key))
            self.__tracking.append(key)
        return

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
