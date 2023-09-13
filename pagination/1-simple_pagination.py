#!/usr/bin/env python3
"""Script takes two args page default 1 and
page_size default 10"""
import csv
from typing import List, Tuple


class Server:
    """Class to paginate the database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method that get page"""
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
