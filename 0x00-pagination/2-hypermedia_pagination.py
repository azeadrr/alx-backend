#!/usr/bin/env python3
"""hypermedia_pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """method named get_page
    integer arguments page with
    default value 1 and page_size
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """class to paginate a db of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                dataset = [row for row in read]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """empty list should be returned"""
        assert all([isinstance(page, int), isinstance(page_size, int)])
        assert page > 0 and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx: end_idx]

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary"""
        data = self.get_page(page, page_size)
        next_page = None if len(self.get_page(
            page + 1, page_size)) else page + 1
        prev_page = None if page - 1 <= 0 else page - 1
        total_pages = len(self.dataset()) / page_size

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(total_pages)
        }
