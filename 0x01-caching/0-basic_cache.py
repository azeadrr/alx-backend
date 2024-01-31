#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data"""
        return self.cache_data.get(key, None)
