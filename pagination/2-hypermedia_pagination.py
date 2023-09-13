#!/usr/bin/env python3
"""Script that implement get_hyper method that takes
same args as get_page and return a dict"""
import csv
from typing import List, Tuple, Dict
from math import ceil


class Server:
    """Class to paginate the database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = self.index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return tuple of size two"""
        end: int = page * page_size
        start: int = end - page_size

        return (start, end)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        totalpag: int = len(dataset) if dataset else 0
        totalpag = ceil(totalpag / page_size)
        prevpag: int = (page - 1) if (page - 1) >= 1 else None
        nextpag: int = (page + 1) if (page + 1) <= totalpag else None

        hypermedia: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextpag,
            'prev_page': prevpag,
            'total_pages': totalpag,
        }

        return hypermedia
