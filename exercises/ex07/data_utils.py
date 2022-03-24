"""Dictionary related utility functions."""

__author__ = "730474696"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Creates a new dictionary that only has the "number" rows of data."""
    result: dict[str, list[str]] = {}
    # if the given number is bigger, than the function will not go through. 
    if number >= len(column_table):
        return column_table
    for column in column_table:
        dict_values: list[str] = []
        i: int = 0
        while i < number:
            # Adds the lists in the dictionary to an empty list. 
            dict_values.append(column_table[column][i])
            i += 1
        # Assigns to the key the empty list from above. 
        result[column] = dict_values
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Creates a new dictionary with the data of only a certain set of columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        # Creates a list of the values of the dictionary and then assigns to a new dictionary that list of values. 
        value: list[str] = column_table[column]
        result[column] = value
    return result


def concat(column_1: dict[str, list[str]], column_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a new dictionary that combines both sets of data into one."""
    result: dict[str, list[str]] = {}
    for column in column_1:
        # Assigns to a new list the key and value from column_1
        result[column] = column_1[column]
    for column in column_2:
        if column in result:
            # Tests to see if the key is already in the result dictionary, and if it is, append the lists together. 
            result[column] += column_2[column]
        else:
            # If the key is not in the result dictionary, then a new key with the list as the value is created. 
            result[column] = column_2[column] 
    return result


def count(given_values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears and assigns that in the dictionary as value: frequency of value."""
    frequencies: dict[str, int] = dict()
    for value in given_values:
        if value in frequencies:
            # if the value is already in frequencies as a key, then the value is increased by one. 
            frequencies[value] += 1
        elif value not in frequencies:
            # Tests to see if the value is in the frequncies dictionary, 
            # and if it's not then the list value is added to the dictionary as a key and assigned a value of one.
            frequencies[value] = 1
    return frequencies
