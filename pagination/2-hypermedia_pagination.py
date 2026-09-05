#!/usr/bin/env python3

"""Hypermedia pagination"""

import csv
import math
from typing import Dict, List, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indexes for a given page_size"""
    start_index = (page - 1) * page_size
    end_index = page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset__ = None

    def dataset(self) -> List[List]:
        """Cache dataset"""
        if self.__dataset__ is None:
            with open(self.DATA_FILE) as f:
                reader = [row for row in reader]
            self.__dataset__ = self.dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:
        """Return a page of the datase based on pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing pairs of hypermedia"""

        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if total_items > 0 else 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
