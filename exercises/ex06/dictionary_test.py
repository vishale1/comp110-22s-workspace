"""Dictionary Test."""

___author___ = "730474696"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color


def test_invert_names() -> None:
    """This test will take a dictionary of first name: last name and return last name: first name."""
    names: dict[str, str] = {'Vishal': 'Erninti', 'Kris': 'Jordan', 'Morgan': 'Freeman'}
    assert invert(names) == {'Erninti': 'Vishal', 'Jordan': 'Kris', 'Freeman': 'Morgan'}


def test_invert_alphabet() -> None:
    """This test will take a dictionary of number: letter and return letter: number."""
    alphabet: dict[str, str] = {"1": "A", "2": "B", "3": "C"}
    assert invert(alphabet) == {"A": "1", "B": "2", "C": "3"}


def test_invert_blank() -> None:
    """This test will return a blank dictionary."""
    blank: dict[str, str] = {}
    assert invert(blank) == {}


def test_count_a() -> None: 
    """ This function returns the number of times a item appears in a list."""
    letters: list[str] = ["a", "b", "b", "c", "c", "c"]
    assert count(letters) == {"a": 1, "b": 2, "c": 3}


def test_count_b() -> None: 
    """ This function returns the number of times a name appears in a list."""
    names: list[str] = ["will", "will", "will", "will", "steve", "ryan"]
    assert count(names) == {"will": 4, "steve": 1, "ryan": 1}


def test_count_c() -> None:
    """This function will only return one item."""
    foods: list[str] = ["pizza"]
    assert count(foods) == {"pizza": 1}


def test_favorite_color_a() -> None:
    """This function will return the most frequent color given a dic of names:colors."""
    colors: dict[str, str] = {"Vishal": "red", "Leo": "red", "Parker": "blue"}
    assert favorite_color(colors) == "red"


def test_favorite__color_b() -> None:
    """This function will return the first most frequent color even if two colors have the same frequency."""
    colors: dict[str, str] = {"Vishal": "red", "Leo": "red", "Parker": "blue", "Gabe": "blue"}
    assert favorite_color(colors) == "red"


def test_c() -> None:
    """This test will return nothing"""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""