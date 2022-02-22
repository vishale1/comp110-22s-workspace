"""Utils Test."""

___author___ = "730474696"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_both() -> None:
    """This test goes through a list of both even and odd and returns only the even numbers."""
    list_a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert only_evens(list_a) == [2, 4, 6, 8, 10, 12, 14, 16]


def test_only_evens_evens() -> None:
    """This test goes through a list of only evens and will return the entire list."""
    list_a: list[int] = [100, 102, 104, 106, 108, 110]
    assert only_evens(list_a) == [100, 102, 104, 106, 108, 110]


def test_only_evens_empty() -> None:
    """This test goes through a list of only odds and will return a empty list."""
    list_a: list[int] = [1, 33, 67, 99, 5, 7]
    assert only_evens(list_a) == []


def test_sub_correct() -> None:
    """This test will return the entire list starting from the beginning to the end ."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_a, 0, 5) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """This test will go through a list and return an empty list since the indices are out of range."""
    list_a: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(list_a, 500, 1000) == []


def test_sub_length() -> None:
    """This test will return the entire list despite the first index being a negative number and the second index being greater than the length of list."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_a, -5, 10) == [1, 2, 3, 4, 5]


def test_concat_both() -> None:
    """This test will return a list with list_a followed by list_b."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    list_b: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_backwards() -> None:
    """This test will return a list with list_b followed by list_a."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    list_b: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_b, list_a) == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


def test_concat_only_one() -> None:
    """This test will return only list_b because list_a is empty."""
    list_a: list[int] = []
    list_b: list[int] = [10, 14, 17, 20, 32]
    assert concat(list_a, list_b) == [10, 14, 17, 20, 32]
