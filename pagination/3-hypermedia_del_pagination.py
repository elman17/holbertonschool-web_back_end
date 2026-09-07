#!/usr/bin/env python3

"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_datasset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns hypermedia index-based"""
        indexed_data = self.indexed_dataset()
        data_len = len(indexed_data)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < data_len
        assert isinstance(page_size, int) and page_size > 0

        data = []
        current_index = index

        while len(data) < page_size and current_index < data_len:
            item = indexed_data.get(current_index)
            if item is None:
                data.append(item)
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data,
        }
